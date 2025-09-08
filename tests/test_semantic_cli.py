# gpt/tests/test_semantic_cli.py

from phred.cli.semantic_cli import run_semantic_cli

def test_semantic_dry_run():
    run_semantic_cli(source="espn", profile="player", identifier="2025", dry_run=True)
    # Optionally capture stdout with capsys
