# gridiron_gpt/cli_registry.py

import importlib
import pkgutil
import gridiron_gpt.cli as cli_pkg
from gridiron_gpt.cli import cli
from gridiron_gpt.feedback import banner_info, banner_warn

def discover_cli_entry():
    banner_info("🔍 Discovering CLI entry point...")
    try:
        assert callable(cli), "CLI entry point is not callable"
        banner_info("✅ CLI entry point is valid.")
        return cli
    except Exception as e:
        banner_warn(f"🚫 CLI discovery failed: {e}")
        raise

def discover_subcommands():
    banner_info("🔍 Scanning CLI subcommands...")
    for _, modname, _ in pkgutil.iter_modules(cli_pkg.__path__):
        try:
            importlib.import_module(f"gridiron_gpt.cli.{modname}")
            banner_info(f"✅ Loaded subcommand: {modname}")
        except Exception as e:
            banner_warn(f"⚠️ Failed to load {modname}: {e}")

def dry_run_cli():
    banner_info("🧪 Dry-run mode: CLI registry check")
    try:
        entry = discover_cli_entry()
        banner_info(f"🎯 CLI entry: {entry.__name__}")
    except Exception as e:
        banner_warn(f"❌ Dry-run failed: {e}")

from gridiron_gpt.cli_registry import dry_run_cli

if __name__ == "__main__":
    dry_run_cli()
