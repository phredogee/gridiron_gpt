from io import StringIO
import sys

def fetch_espn_data(season, limit=10, dry_run=False):
    """Fetch ESPN data or simulate fetch in dry-run mode."""
    if dry_run:
        print("Dry-run mode: No data fetched.")
        return
    # Real fetch logic would go here
    print(f"Fetching ESPN data for season {season} with limit {limit}...")

def test_espn_fetch_dry(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "espn", "--season", "2024", "--limit", "1", "--dry-run"])
    captured_output = StringIO()
    sys.stdout = captured_output
    fetch_espn_data(season="2024", limit=1, dry_run=True)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "dry-run" in output.lower(), f"Expected 'dry-run' in output: {repr(output)}"
