import os
import math
import requests
import pandas as pd
import numpy as np

# --- Config ---
LEAGUE_ID = os.environ.get("SLEEPER_LEAGUE_ID", "").strip() or "123456789012345678"  # <- your real id
SEASON = int(os.environ.get("SEASON", "2025"))
WEEK   = int(os.environ.get("WEEK", "8"))  # set the target NFL week

# --- Sleeper: players metadata (has gsis_id for mapping) ---
from sleeper_wrapper import Players
PLAYERS = Players().get_all_players()  # dict: sleeper_id -> player_dict

def player_name(pid):
    p = PLAYERS.get(pid) or {}
    return p.get("full_name") or p.get("last_name") or pid

def player_team(pid):
    p = PLAYERS.get(pid) or {}
    return p.get("team") or p.get("team_abbr")

def player_pos(pid):
    p = PLAYERS.get(pid) or {}
    fpos = p.get("fantasy_positions") or []
    return ",".join(fpos) if fpos else p.get("position")

def player_gsis(pid):
    p = PLAYERS.get(pid) or {}
    return p.get("gsis_id")  # like "00-0033873"

# --- Sleeper: league endpoints (users, rosters, matchups) ---
API = "https://api.sleeper.app/v1"

def sget(url):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.json()

def get_league_users(league_id):
    return sget(f"{API}/league/{league_id}/users")

def get_league_rosters(league_id):
    return sget(f"{API}/league/{league_id}/rosters")

def get_league_matchups(league_id, week):
    return sget(f"{API}/league/{league_id}/matchups/{week}")

def build_owner_map(users):
    # user_id -> display_name
    return {u["user_id"]: (u.get("display_name") or u.get("username") or u["user_id"])
            for u in users}

def build_roster_owner_map(rosters, owner_map):
    # roster_id -> owner display name
    out = {}
    for r in rosters:
        owner = owner_map.get(r.get("owner_id"), f"Owner:{r.get('owner_id')}")
        out[r["roster_id"]] = owner
    return out

# --- Projections: rolling PPR from nfl_data_py ---
import nfl_data_py as nfl
import pandas as pd

def try_import_weekly(year: int) -> pd.DataFrame | None:
    try:
        df = nfl.import_weekly_data([year])
        # normalize identifier
        return df.rename(columns={"player_id": "gsis_id"})
    except Exception as e:
        print(f"⚠️  weekly data not available for {year}: {e}")
        return None

# Prefer current season; fall back to prior; if early week, include prior to stabilize
cand = [SEASON]
if WEEK <= 3:
    cand.append(SEASON - 1)
# always consider prior season as a hard fallback too
if (SEASON - 1) not in cand:
    cand.append(SEASON - 1)

frames = []
for y in cand:
    df = try_import_weekly(y)
    if df is not None:
        frames.append(df)

if not frames:
    raise RuntimeError("No weekly data available from nfl_data_py for the selected seasons.")

weekly = pd.concat(frames, ignore_index=True)

# Limit to games before the target week in the target SEASON
hist = weekly[weekly["season"] <= SEASON]
if (hist["season"] == SEASON).any():
    hist = hist[~((hist["season"] == SEASON) & (hist["week"] >= WEEK))]

# Limit to games before the target week in the target SEASON where possible
hist = weekly[(weekly["season"] <= SEASON)]
if (hist["season"] == SEASON).any():
    hist = hist[~((hist["season"] == SEASON) & (hist["week"] >= WEEK))]

# Build rolling-average projection by GSIS (last N games; fallback to season avg; final fallback to small prior)
N = 5

def build_projection_table():
    # compute rolling mean fantasy_points_ppr per player (gsis_id)
    hist_sorted = hist.sort_values(["gsis_id", "season", "week"])
    hist_sorted["ppr"] = hist_sorted["fantasy_points_ppr"].astype(float)
    proj = (hist_sorted
            .groupby("gsis_id")["ppr"]
            .apply(lambda s: s.tail(N).mean() if len(s) else np.nan)
            .rename("proj_ppr")
            .to_frame())
    # Reasonable default if truly no history
    proj["proj_ppr"].fillna(6.0, inplace=True)  # bench replacement-level default
    return proj

PROJ = build_projection_table()

def projected_points_for_sleeper_player(sleeper_pid):
    gid = player_gsis(sleeper_pid)
    if not gid:
        return 6.0  # no mapping; replacement-level
    val = PROJ["proj_ppr"].get(gid)
    try:
        return float(val) if pd.notna(val) else 6.0
    except Exception:
        return 6.0

# --- Build Roster Dashboard & Matchup Predictor ---
def build_roster_dashboard(league_id, week):
    users = get_league_users(league_id)
    rosters = get_league_rosters(league_id)
    matchups = get_league_matchups(league_id, week)

    owner_map = build_owner_map(users)
    roster_owner = build_roster_owner_map(rosters, owner_map)

    # Map roster_id -> starters list (Sleeper stores starters as list of sleeper player ids)
    starters_by_roster = {r["roster_id"]: (r.get("starters") or []) for r in rosters}

    # Build matchup pairs by roster_id using the 'matchup_id' field
    by_matchup = {}
    for m in matchups:
        mid = m.get("matchup_id")
        if mid is None:
            # Some leagues have null matchup_id (rare); bucket by roster_id
            mid = f"roster_{m['roster_id']}"
        by_matchup.setdefault(mid, []).append(m["roster_id"])

    rows = []
    team_summaries = {}
    for rid, starters in starters_by_roster.items():
        owner = roster_owner.get(rid, f"Roster {rid}")
        # Sum projections for current starters; skip None or empty slots
        starters = [p for p in starters if p]  # e.g., empty strings for open spots
        projs = [projected_points_for_sleeper_player(p) for p in starters]
        total_proj = float(np.nansum(projs)) if len(projs) else 0.0
        rows.append({
            "roster_id": rid,
            "owner": owner,
            "n_starters": len(starters),
            "proj_total": round(total_proj, 2),
        })
        team_summaries[rid] = dict(total_proj=total_proj, owner=owner)

    dash = pd.DataFrame(rows).sort_values("proj_total", ascending=False).reset_index(drop=True)

    # Build matchup predictions
    match_rows = []
    for mid, rids in by_matchup.items():
        if len(rids) == 2:
            a, b = rids
            ta, tb = team_summaries.get(a, {}), team_summaries.get(b, {})
            pa, pb = ta.get("total_proj", 0.0), tb.get("total_proj", 0.0)

            # Simple uncertainty model: assume team totals ~ Normal(mean, sd)
            # sd ~ 0.2 * mean as a coarse fantasy variance proxy (tweakable)
            sd_a = max(8.0, 0.2 * pa)
            sd_b = max(8.0, 0.2 * pb)

            # Approx win prob for A: P(A > B) where A-B ~ Normal(pa-pb, sqrt(sd_a^2+sd_b^2))
            mean_diff = pa - pb
            sd_diff = math.sqrt(sd_a**2 + sd_b**2)
            z = mean_diff / sd_diff if sd_diff > 1e-6 else 0.0
            # Normal CDF approximation
            win_a = 0.5 * (1.0 + math.erf(z / math.sqrt(2)))
            match_rows.append({
                "matchup_id": mid,
                "A_owner": ta.get("owner", a),
                "B_owner": tb.get("owner", b),
                "A_proj": round(pa, 2),
                "B_proj": round(pb, 2),
                "A_win_prob": round(100 * win_a, 1),
                "B_win_prob": round(100 * (1 - win_a), 1),
            })
        else:
            # bye or odd scenarios
            for rid in rids:
                t = team_summaries.get(rid, {})
                match_rows.append({
                    "matchup_id": mid,
                    "A_owner": t.get("owner", rid),
                    "B_owner": None,
                    "A_proj": round(t.get("total_proj", 0.0), 2),
                    "B_proj": None,
                    "A_win_prob": None,
                    "B_win_prob": None,
                })

    matches = pd.DataFrame(match_rows)

    return dash, matches

def main():
    dash, matches = build_roster_dashboard(LEAGUE_ID, WEEK)
    # Pretty prints
    pd.set_option("display.width", 140)
    pd.set_option("display.max_columns", 20)
    print("\n=== ROSTER DASHBOARD (projected totals from rolling PPR) ===")
    print(dash)

    print(f"\n=== MATCHUP PREDICTOR — SEASON {SEASON}, WEEK {WEEK} ===")
    print(matches.sort_values("matchup_id").reset_index(drop=True))

if __name__ == "__main__":
    main()
