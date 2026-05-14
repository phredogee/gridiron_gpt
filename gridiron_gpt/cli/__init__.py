# gridiron_gpt/cli/__init__.py

'''
┌────────────────────────────────────────────┐
│  Feedback Module Export Map                │
├────────────┬───────────────────────────────┤
│ banner.py  │ render_banner                 │
│ context.py │ FeedbackContext               │
│ core.py    │ generate_feedback             │
│ __init__.py│ Explicit exports via __all__  │
└────────────┴───────────────────────────────┘
'''

from .main import cli, main
from .espn import espn
from gridiron_gpt.feedback import banner_warn
from click.testing import CliRunner

cli.add_command(espn)

def validate_cli_import():
    try:
        from gridiron_gpt.cli import cli
    except ImportError as e:
        banner_warn(f"🚫 CLI import failed: {e}")
        raise

def validate_cli_exposure():
    try:
        from gridiron_gpt.cli import cli
        assert callable(cli), "CLI is not callable"
        print("✅ CLI import and exposure is valid.")
    except Exception as e:
        print(f"🚫 CLI import failed: {e}")

def test_cli_registry_exposure():
    from gridiron_gpt.cli import cli
    runner = CliRunner()
    result = runner.invoke(cli, ["espn", "--help"])
    assert result.exit_code == 0
    assert "intake" in result.output
    assert "dry-run" in result.output
    assert "fix" in result.output
