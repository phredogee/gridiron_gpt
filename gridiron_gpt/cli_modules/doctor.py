# cli/doctor.py

import typer
from pathlib import Path
import shutil
import sys

doctor_app = typer.Typer()

def clean_pycache(verbose: bool = False, dry_run: bool = False):
    pycache_dirs = list(Path(".").rglob("__pycache__"))
    for d in pycache_dirs:
        if dry_run:
            print(f"🧪 [dry-run] Would remove {d}")
        else:
            if verbose:
                print(f"🧹 Removing {d}")
            shutil.rmtree(d, ignore_errors=True)

@doctor_app.command()
def check_imports(verbose: bool = False, dry_run: bool = False):
    """Scan for broken imports and clean __pycache__."""
    print("🧪 Running import diagnostics...\n")

    clean_pycache(verbose=verbose, dry_run=dry_run)

    print("\n📦 Checking module visibility...")
    missing_modules = []

    try:
        from phredenv.pipelines import fetch as score_fetch
        print("✅ phredenv.pipelines.fetch available")
    except ImportError:
        print("❌ phredenv.pipelines.fetch not found")
        missing_modules.append("phredenv.pipelines.fetch")

    try:
        from gridiron_gpt.intake import fetch as player_fetch
        print("✅ gridiron_gpt.intake.fetch available")
    except ImportError:
        print("❌ gridiron_gpt.intake.fetch not found")
        missing_modules.append("gridiron_gpt.intake.fetch")

    if missing_modules:
        print(f"\n❌ Missing modules: {', '.join(missing_modules)}")
        sys.exit(1)
    else:
        print("\n✅ All imports resolved")
        sys.exit(0)

@doctor_app.callback()
def doctor_main():
    print("🩺 Gridiron Doctor — diagnostics and cleanup tools\n")
