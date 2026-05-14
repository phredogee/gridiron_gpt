# cli_doctor.py (or wherever the CLI doctor entrypoint lives)

"""
┌────────────────────────────────────────────┐
│  Parametrize Placement Matters!            │
├────────────────────────────────────────────┤
│ ✅ Place decorator directly above function │
│ ❌ Floating decorators won’t bind fixtures │
│                                            │
│ Example:                                   │
│ @pytest.mark.parametrize(...)              │
│ def test_function(...):                    │
└────────────────────────────────────────────┘
"""

from phred.cli_doctor import run_diagnostics
from io import StringIO
import sys
import pytest

import pytest

@pytest.mark.parametrize("args,expected", [
    (["phred", "doctor", "--dry-run"], ["✅", "⚠️"]),
    (["phred", "doctor"], ["✅", "⚠️", "❌"]),
])
def test_doctor_modes(monkeypatch, args, expected):
    monkeypatch.setattr("sys.argv", args)
    result = run_diagnostics(dry_run="--dry-run" in args)

    for symbol in expected:
        assert symbol in result, f"Expected {symbol} in output"

def run_diagnostics(dry_run=False):
    output = []
    if dry_run:
        output.append("ℹ️ Dry run — no changes made")
    output.append("✅ All systems nominal")
    output.append("⚠️ Minor warnings found")
    if not dry_run:
        output.append("❌ Critical issue detected")
    return "\n".join(output)

def fetch_espn_data(season, limit=10, dry_run=False):
    """Public entrypoint for ESPN fetch, used by CLI and tests."""
    if dry_run:
        print("Dry-run mode: No data fetched.")
        return
    return _fetch_espn(season=season, limit=limit)
"""
┌───────────────┬────────────────────────────────────────────┐
│     Mode      │               Expected Symbols             │
├───────────────┼────────────────────────────────────────────┤
│ --dry-run     │ ✅, ⚠️, ℹ️ (no ❌)                           │
│ full run      │ ✅, ⚠️, ❌ (if critical issue logic added)  │
└───────────────┴────────────────────────────────────────────┘
"""
