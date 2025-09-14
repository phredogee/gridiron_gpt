# phred/sports/local_fetch.py

def fetch_local_data(dry_run=True):
    """Fetch player data from a local source."""
    if dry_run:
        return [
            {"playerId": "P001", "name": "Local Hero", "team": "Sharks", "position": "QB", "score": 95},
            {"playerId": "P002", "name": "Local Star", "team": "Tigers", "position": "WR", "score": 88},
        ]
    raise NotImplementedError("Live local fetch not implemented yet.")
