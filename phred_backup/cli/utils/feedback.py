import sys
import pytest
from phred.cli.utils.feedback.context import feedback_context
from phred.cli.utils.feedback.tips import dry_run_tip, audit_tip, success

def validate_shell_env():
    with feedback_context("🔍 Validating shell environment", level="info"):
        dry_run_tip("Checking for Xonsh/Bash compatibility")
        audit_tip("Looking for PYTHONPATH misconfigurations")
        success("Shell environment looks healthy")

def feedback_context(title: str, level: str = "info"):
    print(banner(f"{title}", level=level))
    print("—" * 40)  # Optional visual separator

def banner(message: str, level: str = "info") -> str:
    icons = {
        "info": "ℹ️",
        "success": "✅",
        "warn": "⚠️",
        "error": "❌",
        "dryrun": "🧪",
        "audit": "📋",
        "default": "🔔"
    }
    return f"{icons.get(level, icons['default'])} {message}"

def dry_run_tip(message: str) -> None:
    """Prints a dry-run diagnostic tip."""
    print(f"🧪 Dry-run: {message}")

def audit_tip(message: str) -> None:
    """Prints a semantic audit message."""
    print(f"📋 Audit: {message}")

def warn(message: str) -> None:
    """Prints a warning with emoji."""
    print(f"⚠️ Warning: {message}", file=sys.stderr)

def success(message: str) -> None:
    """Prints a success message with emoji."""
    print(f"✅ {message}")

def error(message: str) -> None:
    """Prints an error message with emoji."""
    print(f"❌ Error: {message}", file=sys.stderr)

def test_banner(capsys):
    print(banner("Welcome!"))
    captured = capsys.readouterr()
    assert "ℹ️ Welcome!" in captured.out

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
