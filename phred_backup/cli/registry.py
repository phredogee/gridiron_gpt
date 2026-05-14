# phred/cli/registry.py

import typer
from phred.cli.utils.feedback import banner, warn
from phred.sports import diagnose_espn_fetch
from ..semantic.index import validate_index
from datetime import datetime

cli = typer.Typer()

# Central command registry
command_registry = {}

def register_command(name):
    def decorator(func):
        command_registry[name] = func
        return func
    return decorator

def get_registered_commands():
    return list(command_registry.keys())

def run_command(name, *args, **kwargs):
    if name not in command_registry:
        raise ValueError(f"❌ Command '{name}' not found.")
    return command_registry[name](*args, **kwargs)

def list_commands() -> dict:
    """Returns a dictionary of command names and their callables."""
    return command_registry.copy()

def expose_cli():
    """Prints all available CLI commands with onboarding banners."""
    banner("🚀 Welcome to Phred CLI")
    for name in get_registered_commands():
        print(f"🔧 Command available: {name}")

def audit_registry(dry_run=False):
    banner("📋 Auditing CLI Registry")
    if dry_run:
        return {"status": "dry-run", "commands": get_registered_commands()}
    return {"commands": get_registered_commands(), "audit_passed": True}

@register_command("doctor")
def run_diagnostics_cli(dry_run: bool = False):
    run_diagnostics(dry_run=dry_run)

def run_diagnostics(dry_run=False):
    banner("🩺 Running CLI diagnostics...")

    if dry_run:
        print("✅ Dry-run mode: no changes made.")
        return

    print("🔍 Checking ESPN intake...")
    diagnose_espn_fetch()

    print("🧠 Validating semantic index...")
    validate_index()

    print("🎯 Diagnostics complete.")

    with open("diagnostics.log", "w") as log:
        log.write(f"Diagnostics run at {datetime.now().isoformat()}\n")
