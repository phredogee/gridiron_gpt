# phred/sports/espn_diagnostics.py
"""
┌────────────────────────────────────────────┐
│  ESPN Diagnostic Flow                      │
├────────────┬───────────────────────────────┤
│ banner()   │ ℹ️ Diagnostic header           │
│ dry_run    │ ✅ + 🧪 messages, no fetch    │
│ full run   │ fetch_from_espn() → players   │
│ error()    │ ❌ if fetch fails or is empty │
└────────────┴───────────────────────────────┘
"""

from phred.cli.espn import fetch_from_espn
from phred.feedback import banner, success, warning, error


def diagnose_espn_fetch(season=None, dry_run=False):
    banner(f"Diagnosing ESPN fetch for season {season}", emoji="ℹ️")

    if dry_run:
        print("✅ [Pass] Dry-run ESPN fetch simulated")
        print("🧪 [Dry-Run] No live requests made")
        return True

    try:
        data = fetch_from_espn(season=season, dry_run=False)
        if data and "players" in data:
            success(f"Fetched {len(data['players'])} players successfully")
            return True
        else:
            error("No players returned from ESPN fetch")
            return False
    except Exception as e:
        error(f"Error during ESPN fetch: {e}")
        return False

def test_diagnose_espn_dry_run(capsys):
    result = diagnose_espn_fetch(season=2024, dry_run=True)
    captured = capsys.readouterr()
    assert result is True
    assert "🧪 [Dry-Run] No live requests made" in captured.out
