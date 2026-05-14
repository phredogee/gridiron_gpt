# phred/sports/fetch.py

import os
from typing import List, Dict

from phred.sports.fetchers.nfl_api import fetch_from_nfl_api
from phred.sports.fetchers.nflverse import fetch_nfl_events
from phred.sports.merge import merge_events
from phred.sports.tagging import tag_events
from phred.sports.dashboard import prepare_dashboard
from phred.sports.fetchers.espn import diagnose_espn_fetch
HOOKS = {
    "espn": diagnose_espn_fetch
}

def run_fetch(season: int = 2024, dry_run: bool = True) -> dict:
    bios = fetch_from_espn(season=season, dry_run=dry_run)
    events = fetch_from_nfl_api(season=season, dry_run=dry_run)
    nflverse = fetch_nfl_events(season=season, dry_run=dry_run)

    bios_dict = {p["playerId"]: p for p in bios}
    merged_events = merge_events(events, nflverse)
    tagged_events = tag_events(merged_events, bios_dict)
    dashboard = prepare_dashboard(tagged_events, bios)

    if dry_run:
        print(f"\n✅ Dashboard preview:")
        for row in dashboard[:5]:
            name = row.get("name", "Unknown")
            team = row.get("team", "N/A")
            labels = ", ".join(row.get("labels", []))
            count = row.get("event_count", 0)
            print(f"🔹 {name} ({team}) → [{labels}] [{count} events]")

    return {
        "bios": bios,
        "events": tagged_events,
        "dashboard": dashboard
    }

FETCHERS = {
    "espn": fetch_from_espn,
    "nfl_api": fetch_from_nfl_api,
    # Add more sources here as needed
}

def fetch_from_espn(season: int = 2024, dry_run: bool = True) -> list:
    print(f"\n📡 Fetching ESPN bios for season {season}...")
    # Simulated bios
    bios = [
        {"playerId": "101", "name": "J. Jefferson", "team": "MIN", "position": "WR", "rookie": False},
        {"playerId": "102", "name": "C. Stroud", "team": "HOU", "position": "QB", "rookie": True},
    ]
    if dry_run:
        print(f"🧪 Preview: {len(bios)} bios")
        for p in bios:
            print(f"🔹 {p['name']} ({p['team']}, {p['position']})")
    return bios

def fetch_player_data(season: int, source: str = "espn") -> dict:
    source = source.lower()
    print(f"📡 Fetching NFL data from source: {source} for season {season}")
    try:
        fetcher = FETCHERS[source]
    except KeyError:
        print(f"❌ Unknown source—aborting fetch. Available sources: {list(FETCHERS.keys())}")
        return {}

    return fetcher(season)

def fetch_nfl_events(season: int = 2024, dry_run: bool = False) -> List[Dict]:
    if dry_run:
        print("🧪 Dry-run: Simulating NFL event fetch...")
        return [
            {"eventId": "TD001", "type": "touchdown", "playerId": "123", "date": "2024-09-10", "teams": ["SF", "DAL"]},
            {"eventId": "SK002", "type": "sack", "playerId": "456", "date": "2024-09-11", "teams": ["NYJ", "BUF"]},
        ]

    print("📡 Fetching live NFL events...")
    # TODO: Replace with real API call or file read
    return []

if __name__ == "__main__":
    data = run_fetch(dry_run=True)
