
"""
┌────────────────────────────────────────────┐
│  Feedback Test Map                         │
├────────────┬───────────────────────────────┤
│ success()  │ Prints ✅ message             │
│ error()    │ Prints or returns ❌ message  │
│ banner()   │ Maps level → emoji            │
│ context    │ Wraps output in banners       │
└────────────┴───────────────────────────────┘
"""

# gridiron_gpt/tests/test_feedback.py

import pytest
from phred.cli.utils import feedback
from phred.cli.utils.feedback import banner, feedback_context

def test_banner_success(capsys):
    feedback.success("All good")
    captured = capsys.readouterr()
    assert "✅ All good" in captured.out

def test_banner_error(capsys):
    feedback.error("Something broke")
    captured = capsys.readouterr()
    assert "❌ Error: Something broke" in captured.out

@pytest.mark.parametrize("level, icon", [
    ("info", "ℹ️"),
    ("success", "✅"),
    ("warn", "⚠️"),
    ("error", "❌"),
    ("dryrun", "🧪"),
    ("unknown", "ℹ️"),  # fallback case
])
def test_banner_levels(capsys, level, icon):
    banner("Test message", level=level)
    captured = capsys.readouterr()
    assert f"{icon} Test message" in captured.out

def test_feedback_context(capsys):
    with feedback_context("Session Start", level="success"):
        print("Inside context")
    captured = capsys.readouterr()
    assert "✅ Session Start" in captured.out
    assert "Inside context" in captured.out
    assert "—" * 40 in captured.out

