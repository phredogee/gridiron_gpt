# gridiron_gpt/tests/test_feedback.py

import pytest
from modules.utils import EMOJIS
from phred.feedback import render_banner
from phred.feedback.context import FeedbackContext

with FeedbackContext("success") as ctx:
    ctx.log("Your message here")

# ┌────────────────────────────────────────────┐
# │  Feedback Banner Test Map                  │
# ├────────────┬───────────────────────────────┤
# │ Status     │ Expected Symbols              │
# ├────────────┼───────────────────────────────┤
# │ success    │ ✅                            │
# │ warning    │ ⚠️                             │
# │ error      │ ❌                            │
# │ unknown    │ ❓ or fallback                │
# └────────────┴───────────────────────────────┘

EMOJIS = {
    "info": "ℹ️",
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "debug": "🛠️"
}

@pytest.mark.parametrize("status,message,expected", [
    ("success", "Operation completed", "✅"),
    ("warning", "Check configuration", "⚠️"),
    ("error", "Critical failure", "❌"),
    ("unknown", "Mystery status", "❓"),
])
def test_banner_output(status, message, expected):
    banner = render_banner(status, message)
    assert expected in banner
    assert message in banner

def render_banner(status, message):
    emoji = EMOJIS.get(status, "❓")
    if not message:
        message = "No message provided"
    return f"{emoji} {message}"

def test_banner_empty_message():
    banner = render_banner("warning", "")
    assert "⚠️" in banner
    assert "No message provided" in banner

def test_feedback_dry_run():
    from phred.feedback import generate_feedback
    output = generate_feedback(dry_run=True)
    assert "ℹ️ Dry run — no changes made" in output
    assert "✅" in output or "⚠️" in output

def test_feedback_dry_run_logs():
    from phred.feedback import generate_feedback
    logs = generate_feedback(dry_run=True, return_logs=True)
    assert isinstance(logs, list)
    assert any("Dry run" in log for log in logs)

def test_cli_feedback_output(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "feedback", "--dry-run"])
    with pytest.raises(SystemExit):
        from phred.cli import main
        main()

def test_feedback_snapshot(snapshot):
    banner = render_banner("success", "Operation completed")
    snapshot.assert_match(banner, "success_banner")

def test_feedback_context():
    from phred.feedback.context import FeedbackContext
    with FeedbackContext("success") as ctx:
        ctx.log("All systems go")
    assert "✅" in str(ctx)

def test_feedback_context_rule_position():
    from phred.feedback.context import FeedbackContext
    ctx = FeedbackContext("warning")
    ctx.log("Rule misaligned")
    assert "⚠️" in str(ctx)

def test_feedback_context_exception():
    try:
        with FeedbackContext("error") as ctx:
            raise ValueError("Simulated failure")
    except ValueError:
        assert "❌" in str(ctx)

def test_nested_feedback_contexts():
    from phred.feedback.context import FeedbackContext
    with FeedbackContext("success") as outer:
        outer.log("Outer success")
        with FeedbackContext("warning") as inner:
            inner.log("Inner warning")
    assert "✅" in str(outer)
    assert "⚠️" in str(inner)

def test_banner_unknown_status(snapshot):
    banner = render_banner("alien", "Unrecognized status")
    snapshot.assert_match(banner, "unknown_status_banner")
