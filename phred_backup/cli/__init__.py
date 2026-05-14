# ~/gridiron_gpt/phred/cli/__init__.py

from phred.cli.command_registry import command_registry
import importlib
import pkgutil
import os

# 🧠 Command registry for CLI dispatch
command_registry = {}

def register_command(name, help_text=""):
    def decorator(func):
        print(f"Registering command: {name}")
        command_registry[name] = {"func": func, "help": help_text}
        return func
    return decorator

def success(message):
    print(f"✅ {message}")

# 🧪 Optional: Import semantic hooks if not in test mode
if not os.getenv("GRIDIRON_TEST_MODE"):
    try:
        from phred.sports.fetchers.nflverse import fetch_nfl_events
    except ImportError as e:
        print(f"⚠️ Skipping semantic hook: {e}")

# 🔁 Auto-import CLI submodules safely
def _import_cli_modules():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        print(f"Importing CLI module: {modname}")
        try:
            importlib.import_module(f"{__name__}.{modname}")
        except ModuleNotFoundError as e:
            print(f"⚠️ Skipping '{modname}': {e}")

# 🧪 Only import CLI modules if not in test mode
if not os.getenv("GRIDIRON_TEST_MODE"):
    _import_cli_modules()

# 🧪 Placeholder CLI entry point
def main():
    print("🧪 Placeholder function — implement me later")

if __name__ == "__main__":
    main()
