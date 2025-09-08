# phred/sports/espn_diagnostics.py

from .fetch import fetch_from_espn

def diagnose_espn_fetch(season=None, dry_run=False):
    """
    Run a diagnostic check on ESPN fetching.
    Prints pass/fail and dry-run indicators.
    """
    try:
        data = fetch_from_espn(season=season)
        # Basic sanity check
        if data and isinstance(data, list):
            print("✅ [Pass] ESPN fetch returned data.")
        else:
            print("❌ [Fail] ESPN fetch returned no data.")

        if dry_run:
            print("🧪 [Dry-Run] No live fetch performed.")
    except Exception as e:
        print(f"❌ [Fail] Exception during ESPN fetch: {e}")
