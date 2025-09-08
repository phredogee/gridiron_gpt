# gridiron_gpt/tests/test_cli_registry.py

from click.testing import CliRunner
from gridiron_gpt.cli import cli

def test_espn_cli_exposure():
    runner = CliRunner()
    result = runner.invoke(cli, ["espn", "--help"])
    assert result.exit_code == 0
    assert "intake" in result.output
    assert "dry-run" in result.output
    assert "fix" in result.output

def test_cli_exposes_expected_commands():
    commands = cli.commands.keys()
    assert "espn" in commands, "🚫 'espn' subcommand not registered in CLI"
