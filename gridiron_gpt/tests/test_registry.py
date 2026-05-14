# phred/cli/registry.py

from phred.sports.espn import fetch_from_espn  # or your actual ESPN CLI entry point

def list_commands():
    """
    📋 Returns a mapping of CLI command names to their callables.
    """
    return {
        "espn": _espn_fetcher
    }

def run_command(name, *args, **kwargs):
    """
    ▶️ Runs the CLI command by name.
    """
    commands = list_commands()
    if name not in commands:
        raise ValueError(f"❌ Unknown command: {name}")
    return commands[name](*args, **kwargs)
