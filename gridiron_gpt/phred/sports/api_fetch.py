# phred/sports/api_fetch.py

def fetch_api_data(dry_run=True):
    """Fetch player data from an API source."""
    if dry_run:
        return [{"status": "API dry-run", "players": []}]
    raise NotImplementedError("Live API fetch not implemented yet.")
