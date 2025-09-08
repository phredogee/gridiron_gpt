
from io import StringIO
import sys
import pytest

@pytest.mark.parametrize("args,expected", [
    (["phred", "doctor", "--dry-run"], ["✅", "⚠️"]),
    (["phred", "doctor"], ["✅", "⚠️", "❌"]),
])
def test_doctor_modes(monkeypatch, args, expected):
    monkeypatch.setattr("sys.argv", args)
    result = run_diagnostics(dry_run="--dry-run" in args)
    assert any(e in result for e in expected)

def test_espn_fetch_dry(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "espn", "--season", "2024", "--limit", "1", "--dry-run"])
    captured_output = StringIO()
    sys.stdout = captured_output
    fetch_espn_data(season="2024", limit=1, dry_run=True)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "Dry-run mode" in output


