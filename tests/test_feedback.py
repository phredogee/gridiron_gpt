from phred.feedback import banner, feedback_context
from unittest.mock import patch
import pytest
import subprocess

def test_banner_success():
    msg = banner("All systems go", status="success")
    assert "✅" in msg
    assert "All systems go" in msg

def test_banner_warning():
    msg = banner("Caution advised", status="warning")
    assert "⚠️" in msg

def test_banner_error():
    msg = banner("Failure detected", status="error")
    assert "❌" in msg

def emit(self, message: str):
    emojis = {
        "info": "🧠",
        "success": "✅",
        "warn": "⚠️",
        "error": "❌",
        "debug": "🛠️"
    }
    emoji = emojis.get(self.level, "🧠")
    banner_msg = f"\n{emoji} {message}\n{'-' * 40}"
    if divider:
        banner_msg += "-" * 40
    if self.dry_run:
        self.logs.append(f"DRY-RUN: {message}")
    else:
        print(banner_msg, flush=True)

def test_feedback_context(capsys):
    with feedback_context("Testing context", level="success"):
        print("Inside context")
    captured = capsys.readouterr()
    assert "-" * 40 in captured.out

def test_feedback_context_rule_position(capsys):
    with feedback_context("Rule test", level="info"):
        print("Mid-message")
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert lines[0].startswith("ℹ️ Rule test")
    assert lines[-1] == "—" * 40

def test_feedback_context_exception(capsys):
    with pytest.raises(ValueError):
        with feedback_context("Error context", level="error"):
            raise ValueError("Boom")
    captured = capsys.readouterr()
    assert "❌ Error context" in captured.out

def test_nested_feedback_contexts(capsys):
    with feedback_context("Outer", level="warning"):
        with feedback_context("Inner", level="success"):
            print("Deep inside")
    captured = capsys.readouterr()
    assert "⚠️ Outer" in captured.out
    assert "✅ Inner" in captured.out
    assert "Deep inside" in captured.out

def test_banner_unknown_status():
    msg = banner("Unknown status test", status="mystery")
    assert "🔔" in msg or "ℹ️" in msg  # fallback emoji

def test_banner_empty_message():
    msg = banner("", status="success")
    assert "✅" in msg
    assert msg.strip() != "✅"  # should still include some structure

def test_banner_custom_emoji():
    msg = banner("Custom emoji", status="success", emoji="🚀")
    assert "🚀" in msg

def test_feedback_dry_run(capsys):
    with feedback_context("Dry run", level="info", dry_run=True):
        print("Should not appear")
    captured = capsys.readouterr()
    assert "Should not appear" not in captured.out

def test_feedback_dry_run_logs():
    with patch("phred.feedback.logger") as mock_logger:
        with feedback_context("Dry run", dry_run=True):
            pass
    mock_logger.info.assert_called_with("Dry run: Dry run")

def test_cli_feedback_output():
    result = subprocess.run(["phred", "doctor"], capture_output=True, text=True)
    assert "✅" in result.stdout or "⚠️" in result.stdout

EXPECTED = """✅ Testing context
Inside context
----------------------------------------
"""

def test_feedback_snapshot(capsys):
    with feedback_context("Testing context", level="success"):
        print("Inside context")
    captured = capsys.readouterr()
    assert captured.out.strip() == EXPECTED.strip()
