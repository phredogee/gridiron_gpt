

"""
⚙️ Phred CLI Package — Contributor Onboarding

This package contains CLI entry points for:
- 🏈 sports analytics workflows (`gridiron`)
- 🧪 dry-run diagnostics
- 📊 feedback rendering and context management

Main entry point:
    $ gridiron

Defined in:
    pyproject.toml → [project.scripts]
    gridiron = "phred.cli.main:app"

To add a new CLI tool:
1. Create a new module in `phred/cli/` (e.g. `stats.py`)
2. Define `def app(): ...`
3. Register it in pyproject.toml under [project.scripts]

To test CLI locally:
    $ python -m phred.cli.main --dry-run

Happy CLI hacking! 🛠
"""
__all__ = ["main"]

def cli_status():
    print("✅ Phred CLI loaded successfully")
