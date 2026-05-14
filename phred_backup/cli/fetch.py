# ~/gridiron_gpt/phred/cli/fetch.py

import argparse
from phred.cli import register_command
from phred.sports.fetch import fetch_nfl_events
from phred.sports.dashboard import prepare_dashboard
from phred.sports.tagging import tag_events
from phred.sports.fetchers.espn import get_player_bios, get_all_player_ids
from phred.utils.banner_utils import banner

@register_command("espn", help_text="Run ESPN bios fetch")
def espn_main():
    parser = argparse.ArgumentParser(prog="phred espn", description="Fetch ESPN bios")
    parser.add_argument("--season", type=int, default=2024)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    banner(f"📡 Fetching player bios for season {args.season}", kind="info")
    players = get_all_player_ids(season=args.season)[:args.limit]
    bios = get_player_bios(players)
    banner(f"✅ Fetched {len(bios)} bios", kind="success")

    events = fetch_nfl_events(args.season)
    if not events:
        banner("🕳️ No events returned — check data source or season", kind="warn")
        return

    bios_dict = {p["playerId"]: p for p in bios}
    tagged_events = tag_events(events, bios_dict)
    dashboard = prepare_dashboard(tagged_events, bios)

    if args.dry_run:
        banner(f"🧪 Previewing {len(bios_dict)} bios", kind="debug")
        for pid, pdata in list(bios_dict.items())[:args.limit]:
            name = pdata.get("name", "Unknown")
            team = pdata.get("team", "N/A")
            print(f"🔹 {pid}: {name} ({team})")

        banner("📋 Event Summary", kind="info")
        for i, info in enumerate(events[:args.limit]):
            eid = info.get("eventId", f"#{i}")
            etype = info.get("type", "Unknown")
            pid = info.get("playerId", "N/A")
            date = info.get("date", "Unknown date")
            teams = " vs ".join(info.get("teams", []))
            print(f"• {date}: {teams} — {etype} by Player {pid} [ID: {eid}]")

def get_all_player_ids(season: int) -> list:
    # TODO: Replace with real ESPN API call
    print(f"📡 Fetching player IDs for season {season}")
    return [
        {"playerId": "123", "name": "John Doe", "team": "NYG"},
        {"playerId": "456", "name": "Jane Smith", "team": "DAL"},
        {"playerId": "789", "name": "Alex Johnson", "team": "BUF"},
    ]

def fetch_nfl_events(season: int, dry_run: bool = False) -> list:
    if dry_run:
        print("🧪 Dry-run: Simulating NFL event fetch...")
        return [
            {"eventId": "evt1", "playerId": "123", "type": "touchdown", "date": "2024-09-01", "teams": ["NYG", "DAL"]},
            {"eventId": "evt2", "playerId": "456", "type": "sack", "date": "2024-09-02", "teams": ["DAL", "BUF"]}
        ]

    print(f"📡 Fetching live NFL events for season {season}...")
    # TODO: Add real API call or file read
    return []
