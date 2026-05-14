# phred/sports/fetchers/espn/fetch.py

from typing import List, Dict

def get_all_player_ids(season: int, dry_run: bool = True) -> List[Dict]:
    """
    Fetch all ESPN player IDs for a given season.

    Args:
        season (int): The season year (e.g., 2024).
        dry_run (bool): If True, returns stubbed data.

    Returns:
        List[Dict]: List of player metadata dictionaries.
    """
    if dry_run:
        print(f"🧪 [Dry-Run] Simulating ESPN fetch for season {season}")
        return [
            {"playerId": 101, "name": "Patrick Mahomes", "team": "Chiefs"},
            {"playerId": 102, "name": "Jalen Hurts", "team": "Eagles"},
            {"playerId": 103, "name": "Christian McCaffrey", "team": "49ers"}
        ]

    # TODO: Implement live ESPN scraping or API call
    print(f"📡 [Live] Fetching ESPN player IDs for season {season}")
    return []

def fetch_from_espn(season: int, dry_run: bool = True) -> Dict:
    """
    Semantic wrapper for ESPN player intake.

    Args:
        season (int): The season year.
        dry_run (bool): If True, uses stubbed data.

    Returns:
        Dict: Structured ESPN player data.
    """
    print(f"📦 Fetching ESPN data for season {season} (dry_run={dry_run})")
    player_ids = get_all_player_ids(season, dry_run=dry_run)
    return {
        "season": season,
        "players": player_ids,
        "count": len(player_ids)
    }
