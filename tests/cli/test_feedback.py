import pytest
from phred.cli.utils import feedback

def test_banner_success(capsys):
    feedback.success("All good")
    captured = capsys.readouterr()
    assert "✅ All good" in captured.out

def test_banner_error():
    assert feedback.error("Something broke") == "❌ Error: Something broke"

@pytest.mark.parametrize("level, icon", [
    ("info", "ℹ️"),
    ("success", "✅"),
    ("warn", "⚠️"),
    ("error", "❌"),
    ("dryrun", "🧪"),
    ("unknown", "ℹ️"),  # fallback case
])

def test_banner_levels(capsys, level, icon):
    print(banner("Test message", level=level))
    captured = capsys.readouterr()
    assert f"{icon} Test message" in captured.out

def test_feedback_context(capsys):
    with feedback_context("Session Start", level="success"):
        print("Inside context")
    captured = capsys.readouterr()
    assert "✅ Session Start" in captured.out
    assert "Inside context" in captured.out
    assert "—" * 40 in captured.out

print(feedback.banner("Test message", level=level))
with feedback.feedback_context("Session Start", level="success"):
