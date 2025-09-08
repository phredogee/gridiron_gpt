# phred/sports/fetch.py

print(">>> starting fetch.py")

from .local_fetch import fetch_local_data
from .api_fetch import fetch_api_data
from .scrape_fetch import fetch_scrape_data

# Lazy import wrapper to avoid circular import issues
def _espn_fetcher(*args, **kwargs):
    from .espn import fetch_from_espn
    return fetch_from_espn(*args, **kwargs)

def get_all_player_ids(season=2024, dry_run=True):
    if dry_run:
        return [
            {"playerId": "P001", "name": "John Doe", "team": "Sharks", "position": "QB", "score": 95},
            {"playerId": "P002", "name": "Jane Smith", "team": "Tigers", "position": "WR", "score": 88},
        ]
    raise NotImplementedError("Live ESPN player ID fetch not implemented yet.")

def get_player_bios(players, dry_run=True):
    if dry_run:
        return [
            {"name": p["name"], "bio": f"{p['name']} is a {p['position']} for the {p['team']}."}
            for p in players
        ]
    raise NotImplementedError("Live player bio fetch not implemented yet.")

def fetch_player_data(*args, **kwargs):
    raise NotImplementedError("fetch_player_data not implemented yet.")

def run_fetch(*args, **kwargs):
    raise NotImplementedError("run_fetch not implemented yet.")

FETCHERS = {
    "local": fetch_local_data,
    "api": fetch_api_data,
    "scrape": fetch_scrape_data,
    "espn": _espn_fetcher,  # safe callable
}

print(">>> finished fetch.py")
