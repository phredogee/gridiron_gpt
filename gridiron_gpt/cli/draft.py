# gridiron_gpt/cli/draft.py

import click
import pandas as pd
from gridiron_gpt.draft.config import LeagueConfig
from gridiron_gpt.draft.ranker import build_rankings, get_round_targets
from gridiron_gpt.feedback import banner, error


@click.group()
def draft():
    """🏆 Pre-season draft tools — rank, strategize, and build your board"""
    pass


@draft.command()
@click.option("--position", "-p", default=None, help="Filter by position (QB, RB, WR, TE, K, DEF)")
@click.option("--top", default=30, show_default=True, type=int, help="Number of players to show")
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--teams", default=12, show_default=True, type=int, help="League size")
@click.option("--rounds", default=15, show_default=True, type=int, help="Number of draft rounds")
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def rank(position, top, scoring, teams, rounds, changes_path):
    """📋 Rank players for the upcoming draft"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)
    try:
        df = build_rankings(config, changes_path=changes_path)
    except Exception as e:
        error(str(e))
        return

    if position:
        df = df[df["position"].str.upper() == position.upper()]
        if df.empty:
            banner(f"No players found for position: {position}", emoji="❓")
            return

    df = df.head(top)

    click.echo(f"\n🏆  Draft Rankings — {scoring.upper()}, {teams}-team\n")
    click.echo(f"  {'#':<4} {'Name':<26} {'Pos':<5} {'Team':<5} {'Hist':>6} {'ADP':>6} {'Score':>7}  Notes")
    click.echo("  " + "─" * 78)

    for _, row in df.iterrows():
        adp_str = f"{row['adp']:.1f}" if row["adp"] is not None else "—"
        note_parts = []
        inj = row.get("injury")
        if inj and not pd.isna(inj):
            note_parts.append(f"[{inj}]")
        note_val = row.get("note")
        if note_val and not pd.isna(note_val):
            note_parts.append(str(note_val))
        mult = row.get("multiplier", 1.0)
        if mult and mult != 1.0:
            note_parts.append(f"×{mult:.2f}")
        note = " ".join(note_parts)
        click.echo(
            f"  {int(row['rank']):<4} {row['name']:<26} {row['position']:<5} {row['team']:<5}"
            f" {row['hist_score']:>6.1f} {adp_str:>6} {row['composite']:>7.1f}  {note}"
        )
    click.echo()


@draft.command()
@click.option("--round", "round_num", required=True, type=int, help="Draft round number (1–15)")
@click.option("--teams", default=12, show_default=True, type=int)
@click.option("--rounds", default=15, show_default=True, type=int)
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def strategy(round_num, teams, rounds, scoring, changes_path):
    """🧠 Draft strategy and top targets for a specific round"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)
    targets, advice = get_round_targets(round_num, config)

    pick_start = (round_num - 1) * teams + 1
    pick_end = round_num * teams

    click.echo(f"\n🧠  Round {round_num} Strategy — {scoring.upper()}, {teams}-team\n")
    click.echo(f"  Picks:    #{pick_start}–#{pick_end}")
    click.echo(f"  Targets:  {', '.join(targets)}")
    click.echo(f"  Advice:   {advice}")

    try:
        df = build_rankings(config, changes_path=changes_path)
        available = df[
            (df["suggested_round"] == round_num) & (df["position"].isin(targets))
        ].head(5)

        if not available.empty:
            click.echo(f"\n  Top available in round {round_num}:")
            for _, row in available.iterrows():
                adp_str = f"ADP {row['adp']:.1f}" if row["adp"] is not None else "undrafted"
                click.echo(f"    #{int(row['rank']):<4} {row['name']:<25} {row['position']:<5} {adp_str}")
    except Exception:
        pass

    click.echo()


@draft.command()
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--teams", default=12, show_default=True, type=int)
@click.option("--rounds", default=15, show_default=True, type=int)
@click.option("--top", default=200, show_default=True, type=int, help="Max players to show")
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def board(scoring, teams, rounds, top, changes_path):
    """📌 Full draft board grouped by suggested round"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)

    try:
        df = build_rankings(config, changes_path=changes_path)
    except Exception as e:
        error(str(e))
        return

    df = df.head(top)

    banner(f"📌 Draft Board — {scoring.upper()}, {teams}-team, {rounds} rounds")
    click.echo(f"  Roster: {config.roster}")
    click.echo(f"  Lineup: {config.lineup}\n")

    current_round = 0
    for _, row in df.iterrows():
        r = int(row["suggested_round"])
        if r != current_round:
            current_round = r
            targets, advice = get_round_targets(current_round, config)
            click.echo(f"\n  ── Round {current_round}  (Target: {', '.join(targets)}) ──")
            click.echo(f"     {advice}\n")

        adp_val = row["adp"]
        adp_str = f"ADP {adp_val:.1f}" if adp_val is not None and not pd.isna(adp_val) else "no ADP"
        note_parts = []
        inj = row.get("injury")
        if inj and not pd.isna(inj):
            note_parts.append(f"[{inj}]")
        note_val = row.get("note")
        if note_val and not pd.isna(note_val):
            note_parts.append(str(note_val))
        note = "  " + " ".join(note_parts) if note_parts else ""

        click.echo(
            f"  #{int(row['rank']):<4} {row['name']:<26} {row['position']:<5} {row['team']:<5}"
            f" {row['hist_score']:>6.1f}pts  {adp_str}{note}"
        )

    click.echo()


@draft.command()
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--season", default=2025, show_default=True, type=int,
              help="Season year to index")
def index(scoring, season):
    """🗂️ Build the ask-query index from historical player stats (offseason use)"""
    import nflreadpy as nfl
    from gridiron_gpt.core.advisor import Advisor

    score_col = "fantasy_points_ppr" if scoring != "standard" else "fantasy_points"

    print(f"📊 Loading {season} player stats...")
    df = nfl.load_player_stats(seasons=[season])
    if hasattr(df, "to_pandas"):
        df = df.to_pandas()

    if score_col not in df.columns:
        score_col = "fantasy_points_ppr" if "fantasy_points_ppr" in df.columns else "fantasy_points"

    agg = (
        df.groupby(["player_display_name", "position", "team"])
        .agg(total_pts=(score_col, "sum"), games=(score_col, "count"))
        .reset_index()
    )
    agg = agg[agg["total_pts"] > 0].sort_values("total_pts", ascending=False)

    pos_names = {
        "QB": "quarterback", "RB": "running back", "WR": "wide receiver",
        "TE": "tight end", "K": "kicker",
    }
    team_names = {
        "ARI": "Arizona Cardinals", "ATL": "Atlanta Falcons", "BAL": "Baltimore Ravens",
        "BUF": "Buffalo Bills", "CAR": "Carolina Panthers", "CHI": "Chicago Bears",
        "CIN": "Cincinnati Bengals", "CLE": "Cleveland Browns", "DAL": "Dallas Cowboys",
        "DEN": "Denver Broncos", "DET": "Detroit Lions", "GB": "Green Bay Packers",
        "HOU": "Houston Texans", "IND": "Indianapolis Colts", "JAX": "Jacksonville Jaguars",
        "KC": "Kansas City Chiefs", "LAC": "Los Angeles Chargers", "LA": "Los Angeles Rams",
        "LV": "Las Vegas Raiders", "MIA": "Miami Dolphins", "MIN": "Minnesota Vikings",
        "NE": "New England Patriots", "NO": "New Orleans Saints", "NYG": "New York Giants",
        "NYJ": "New York Jets", "PHI": "Philadelphia Eagles", "PIT": "Pittsburgh Steelers",
        "SEA": "Seattle Seahawks", "SF": "San Francisco 49ers", "TB": "Tampa Bay Buccaneers",
        "TEN": "Tennessee Titans", "WAS": "Washington Commanders",
    }

    players = []
    for _, row in agg.iterrows():
        name = row["player_display_name"]
        pos_code = str(row["position"]).upper()
        pos = pos_names.get(pos_code, pos_code.lower())
        team = str(row["team"])
        team_name = team_names.get(team, team)
        pts = float(row["total_pts"])
        games = int(row["games"])
        ppg = pts / games if games > 0 else 0
        players.append({
            "player_name": name,
            "position": pos_code,
            "team": team,
            "week": f"{season} season ({games} games)",
            "fantasy_points": pts,
            "surface": f"{ppg:.1f} pts/game average",
            "environment": f"{season} full season",
        })

    advisor = Advisor()
    advisor.build_from_players(players)
    advisor.save()
    click.echo(f"✅ Indexed {len(players)} players from {season} season — ask is ready.")
