# gpt/tests/test_registry.py

from phred.cli.registry import list_commands, run_command

def test_registry_exposes_espn():
    commands = list_commands()
    assert "espn" in commands
    assert callable(commands["espn"])

def test_run_espn_dry_run(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "espn", "--season", "2024", "--dry-run", "--limit", "2"])
    try:
        run_command("espn")
    except SystemExit:
        pass  # argparse may exit after parsing
