# cli_modules/__init__.py

"""
📦 CLI Modules Package — Contributor Onboarding

This package contains modular CLI entry points for:
- 🧠 semantic routing (`semantic-router`)
- 📎 embedding workflows (`embed-cli`)
- 🔄 environment resets (`reset-cli`)
- 📊 dashboard utilities (`dashboard-cli`)

Each module defines an `app()` function exposed via [project.scripts] in pyproject.toml.

Usage:
    $ semantic-router
    $ embed-cli
    $ reset-cli
    $ dashboard-cli

To add a new CLI:
1. Create a new module (e.g. `new_tool.py`)
2. Define `def app(): ...`
3. Register it in pyproject.toml under [project.scripts]

Happy CLI hacking! 🚀
"""
__all__ = [
    "semantic_router",
    "embed_cli",
    "reset",
    "dashboard_cli"
]

def cli_modules_status():
    print("✅ CLI modules loaded successfully")
