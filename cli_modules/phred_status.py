# gridiron_gpt/cli_modules/phred_status.py

import typer
from phredenv.utils import is_xonsh_shell
from phredenv.loader import get_status_report
from phredenv.banner import show_banner

app = typer.Typer(help="""
🧪 Phredenv Session Diagnostics

Usage:
  phred-status --debug
  phred-status --dry-run
""")

@app.command()
def status(debug: bool = False, dry_run: bool = False):
    """Show phredenv session status and diagnostics."""
    print("🧪 [phred-status] Checking shell context...")
    print("🔍 Shell type:", "Xonsh ✅" if is_xonsh_shell() else "Python ❌")

    if dry_run:
        print("🧪 Dry-run mode: skipping banner and report generation")
        return

    if debug:
        print("🐛 Debug mode enabled — showing banner")
        show_banner()

    print("📊 Status Report:")
    print(get_status_report())

if __name__ == "__main__":
    app()
