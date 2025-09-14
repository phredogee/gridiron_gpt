# phred/sports/espn_diagnostics.py

from phred.feedback import banner
from phred.sports.espn import fetch_from_espn

def diagnose_espn_fetch(season=None, dry_run=False):
    """
    Diagnose ESPN data fetching for a given season.

    Args:
        season (int, optional): The season year.
        dry_run (bool): If True, simulate the fetch for testing.

    Returns:
        bool: True if diagnostics pass, False otherwise.
    """
    banner(f"Diagnosing ESPN fetch for season {season}", level="info")

    if dry_run:
        print("✅ [Pass] Dry-run ESPN fetch simulated")
        return True

    try:
        data = fetch_from_espn(season=season, dry_run=False)
        if data and "players" in data:
            banner(f"Fetched {len(data['players'])} players successfully", level="success")
            return True
        else:
            banner("No players returned from ESPN fetch", level="error")
            return False
    except Exception as e:
        banner(f"Error during ESPN fetch: {e}", level="error")
        return False
