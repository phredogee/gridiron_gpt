"""
📦 phred.sports.fetch — Central Fetcher Registry

Handles data intake from multiple sources:
- 🗂 Local files
- 🌐 APIs
- 🕸 Scrapers
- 🏈 ESPN (via lazy import to avoid circular dependencies)

Includes dry-run helpers for onboarding, testing, and contributor diagnostics.
"""

print("🎯 Initializing fetch modes...")

# --- Direct imports ---
from .local_fetch import fetch_local_data
from .api_fetch import fetch_api_data
from .scrape_fetch import fetch_scrape_data

# --- Lazy ESPN fetcher to avoid circular imports ---
def _espn_fetcher(*args, **kwargs):
    try:
        from phred.sports.espn import fetch_from_espn
        return fetch_from_espn(*args, **kwargs)
    except ImportError as e:
        print(f"⚠️ ESPN fetcher unavailable: {e}")
        raise NotImplementedError("ESPN fetcher could not be imported.")

# --- Central registry ---
FETCHERS = {
    "local": fetch_local_data,
    "api": fetch_api_data,
    "scrape": fetch_scrape_data,
    "espn": _espn_fetcher,  # ✅ avoids NameError and circular imports
}

# --- Dry-run helpers ---
def get_all_player_ids(season: int = 2024, dry_run: bool = True):
    """Return mock player data for dry-run mode."""
    if dry_run:
        return [
            {"playerId": "P001", "name": "John Doe", "team": "Sharks", "position": "QB", "score": 95},
            {"playerId": "P002", "name": "Jane Smith", "team": "Tigers", "position": "WR", "score": 88},
        ]
    raise NotImplementedError("Live ESPN player ID fetch not implemented yet.")

def get_player_bios(players: list, dry_run: bool = True):
    """Return mock bios for dry-run mode."""
    if dry_run:
        return [
            {"name": p["name"], "bio": f"{p['name']} is a {p['position']} for the {p['team']}."}
            for p in players
        ]
    raise NotImplementedError("Live player bio fetch not implemented yet.")

def get_dry_run_payload(season: int):
    """Return consistent ESPN-style dry-run payload."""
    return {
        "season": season,
        "source": "dry-run",
        "players": get_all_player_ids(season=season, dry_run=True)
    }

# --- Placeholders for live fetch routines ---
def fetch_player_data(*args, **kwargs):
    raise NotImplementedError("fetch_player_data not implemented yet.")

def run_fetch(*args, **kwargs):
    raise NotImplementedError("run_fetch not implemented yet.")

# --- Validation utility ---
def validate_fetchers():
    """Run each fetcher in dry-run mode (if supported) and print results."""
    print("🧪 Validating fetcher registry...")
    for mode, fetcher in FETCHERS.items():
        try:
            if hasattr(fetcher, "__code") and "dry_run" in fetcher.__code__.co_varnames:
                fetcher(dry_run=True)
            else:
                fetcher()
            print(f"✅ {mode} fetcher executed successfully.")
        except Exception as e:
            print(f"❌ {mode} fetcher failed: {e}")

    try:
        payload = get_dry_run_payload(season=2025)
        print(f"📦 Dry-run payload generated with {len(payload['players'])} players.")
    except Exception as e:
        print(f"❌ Dry-run payload failed: {e}")
