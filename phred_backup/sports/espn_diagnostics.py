# phred/sports/doctor.py

from phred.sports.fetchers.espn.fetch import fetch_from_espn

def diagnose_espn_fetch(season: int = 2024, dry_run: bool = True) -> None:
    """
    Validates ESPN fetcher logic and outputs diagnostic feedback.

    Args:
        season (int): Season year to test.
        dry_run (bool): Whether to simulate fetch.
    """
    print("🔍 [Doctor] Running ESPN fetch diagnostics...")
    try:
        data = fetch_from_espn(season, dry_run=dry_run)
        assert isinstance(data, dict), "Expected dict output"
        assert "players" in data and isinstance(data["players"], list), "Missing or invalid 'players' key"
        assert "count" in data and isinstance(data["count"], int), "Missing or invalid 'count' key"

        print(f"✅ [Pass] ESPN fetch returned {data['count']} players for season {season}")
        if dry_run:
            print("🧪 [Dry-Run] Stubbed data validated successfully")
        else:
            print("📡 [Live] Live fetch logic executed (check for real data)")
    except Exception as e:
        print(f"❌ [Fail] ESPN fetch diagnostic failed: {e}")
