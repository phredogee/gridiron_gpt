# phred/cli/command_registry.py

# phred/cli/command_registry.py

import typer
from phred.cli.utils.feedback import banner
from phred.sports import diagnose_espn_fetch
from phred.semantic.index import validate_index
from datetime import datetime

cli = typer.Typer()
command_registry = {}

# Decorator-based registration
def register_command(name=None):
    def decorator(func):
        cmd_name = name or func.__name__
        print(f"🔧 Registering command: {cmd_name}")
        command_registry[cmd_name] = {
            "func": func,
            "help": func.__doc__ or "No description"
        }
        return func
    return decorator

# Centralized setup (optional)
def setup_commands():
    from phred.cli.some_module import run_something
    register_command("run_something")(run_something)

# Registry utilities
def get_registered_commands():
    return list(command_registry.keys())

def run_command(name, *args, **kwargs):
    if name not in command_registry:
        raise ValueError(f"❌ Command '{name}' not found.")
    return command_registry[name]["func"](*args, **kwargs)

def list_commands():
    return command_registry.copy()

def expose_cli():
    banner("🚀 Welcome to Phred CLI")
    for name in get_registered_commands():
        print(f"🔧 Command available: {name}")

# Example command
@register_command("doctor")
def run_diagnostics_cli(dry_run: bool = False):
    banner("🩺 Running CLI diagnostics...")

    if dry_run:
        print("✅ Dry-run mode: no changes made.")
        return

    print("🔍 Checking ESPN intake...")
    try:
        diagnose_espn_fetch()
        print("✅ ESPN intake check passed.")
    except Exception as e:
        print(f"❌ ESPN intake failed: {e}")

    print("🧠 Validating semantic index...")
    try:
        validate_index()
        print("✅ Semantic index valid.")
    except Exception as e:
        print(f"⚠️ Index validation issue: {e}")

    print("🎯 Diagnostics complete.")
    with open("diagnostics.log", "w") as log:
        log.write(f"Diagnostics run at {datetime.now().isoformat()}\n")
