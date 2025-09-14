# phred/sports/espn.py

"""
🏈 phred.sports.espn — ESPN Data Fetcher

Handles ESPN-specific data intake for player stats, bios, and metadata.
Supports dry-run mode for testing and contributor onboarding.

Live fetch routines are stubbed for future implementation.
"""

print("📡 ESPN fetcher initialized")

# --- Dry-run: Player ID fetch ---
def get_all_player_ids(season: int, dry_run: bool = False):
    """
    Return a list of player dictionaries for the given season.
    Each dict includes: 'playerId', 'name', 'team'.

    In dry_run mode, returns dummy data without hitting ESPN.
    """
    if dry_run:
        return [
            {"playerId": "p1", "name": "Player One", "team": "Team A"},
            {"playerId": "p2", "name": "Player Two", "team": "Team B"},
            {"playerId": "p3", "name": "Player Three", "team": "Team C"},
        ]
    raise NotImplementedError("Live ESPN player ID fetch not implemented yet.")

# --- Dry-run: Player bios ---
def get_player_bios(players: list, dry_run: bool = False):
    """
    Given a list of player dicts, return enriched bios.

    In dry_run mode, returns dummy bios for testing.
    """
    if dry_run:
        return [
            {
                "playerId": p.get("playerId", "unknown"),
                "bio": f"Bio for {p.get('name', 'Unnamed')}",
                "position": p.get("position", "Unknown Position"),
                "team": p.get("team", "Unknown Team")
            }
            for p in players
        ]
    raise NotImplementedError("Live ESPN bio fetching not implemented yet.")

# --- Dry-run: Full ESPN payload ---
def fetch_from_espn(season: int = 2025, dry_run: bool = False):
    """
    Fetch ESPN player data for a given season.

    In dry_run mode, returns mock data for testing.
    """
    if dry_run:
        print(f"🧪 Dry-run mode active for season {season}")
        players = [
            {
                "playerId": f"P{i+1:03}",
                "name": f"Test Player {i+1}",
                "team": "Testers",
                "position": "QB",
                "score": 100 - i
            }
            for i in range(10)
        ]
        return {
            "season": season,
            "players": players,
            "count": len(players),
            "dry_run": True
        }
    raise NotImplementedError("Live ESPN fetch not implemented yet.")
