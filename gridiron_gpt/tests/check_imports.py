# check_imports.py

import os
import sys

def banner(msg, emoji="✅"):
    print(f"{emoji} {msg}")

def check_pythonpath():
    root = os.path.abspath(os.path.join(__file__, "../../.."))
    if root not in sys.path:
        banner(f"Missing PYTHONPATH entry: {root}", "⚠️")
    else:
        banner("PYTHONPATH includes project root")

def check_init_files():
    rel_paths = [
        "../../phred/__init__.py",
        "../../phred/cli/__init__.py",
        "../../phred/cli/utils/__init__.py",
    ]
    for rel in rel_paths:
        full = os.path.abspath(os.path.join(__file__, rel))
        if not os.path.exists(full):
            banner(f"Missing: {full}", "❌")
        else:
            banner(f"Found: {full}")

def check_import():
    try:
        from phred.cli.utils import feedback
        banner("Import succeeded 🧠")
    except Exception as e:
        banner(f"Import failed: {e}", "🔥")

if __name__ == "__main__":
    check_pythonpath()
    check_init_files()
    check_import()
