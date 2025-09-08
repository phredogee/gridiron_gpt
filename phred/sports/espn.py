# phred/sports/espn.py

def fetch_from_espn(season=2024, dry_run=True):
    """
    Fetch player data from ESPN.

    In dry_run mode, returns predictable data for tests and onboarding.
    If dry_run is False, raises a friendly, contributor‑oriented message.
    """
    if dry_run:
        return [
            {"playerId": "P001", "name": "John Doe", "team": "Sharks", "position": "QB", "score": 95},
            {"playerId": "P002", "name": "Jane Smith", "team": "Tigers", "position": "WR", "score": 88},
        ]

    raise RuntimeError(
        "🚧 ESPN live fetch not implemented yet.\n"
        "💡 Tip: Run with dry_run=True for predictable test data.\n"
        "📚 See CONTRIBUTING.md for how to implement live ESPN integration."
    )
