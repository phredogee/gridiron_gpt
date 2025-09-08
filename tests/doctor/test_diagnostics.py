# tests/doctor/test_diagnostics.py

from phred.sports.espn_diagnostics import diagnose_espn_fetch

def test_diagnose_espn_fetch_dry_run(capsys):
    diagnose_espn_fetch(season=2024, dry_run=True)
    captured = capsys.readouterr()
    assert "✅ [Pass]" in captured.out
    assert "🧪 [Dry-Run]" in captured.out

def fetch_from_espn(season=None):
    """
    Fetch player data from ESPN.
    For now, this is a stub that returns fake data in dry-run contexts.
    """
    # In a real implementation, you'd call ESPN's API or scrape.
    return [{"player": "Sample Player", "season": season}]
