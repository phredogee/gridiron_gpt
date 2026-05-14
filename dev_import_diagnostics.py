# my_project/dev_import_diagnostics.py

import ast
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEST_DIR = ROOT / "gridiron_gpt" / "tests"
PHRED_DIR = ROOT / "gridiron_gpt" / "phred"
TARGET_PACKAGE = "phred"

def scan_imports():
    print("🔍 Scanning test files for import issues...\n")
    for file in TEST_DIR.glob("test_*.py"):
        try:
            tree = ast.parse(file.read_text(), filename=str(file))
        except SyntaxError as e:
            print(f"❌ {file.name}: Syntax error — {e}")
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                if mod.startswith(".."):
                    print(f"⚠️ {file.name}: Relative import → `from {mod}`")
                elif not mod.startswith(TARGET_PACKAGE):
                    print(f"❓ {file.name}: Possibly unresolved import → `from {mod}`")
        print(f"✅ {file.name}: scanned\n")

def check_init_files():
    print("📦 Checking for missing __init__.py files...\n")
    missing = []
    for path in PHRED_DIR.rglob("*"):
        if path.is_dir():
            init = path / "__init__.py"
            if not init.exists():
                missing.append(init)
                print(f"⚠️ Missing: {init.relative_to(ROOT)}")
    if not missing:
        print("✅ All package folders have __init__.py\n")

def validate_editable_install():
    print("🧠 Validating editable install...\n")
    try:
        import phred
        print("✅ `phred` is importable — install path looks good")
    except ModuleNotFoundError:
        print("❌ `phred` not importable — check PYTHONPATH or editable install")

def check_setup_py_conflict():
    print("🛠️ Checking for legacy setup.py interference...\n")
    legacy = ROOT / "gridiron_gpt" / "setup.py"
    if legacy.exists():
        print(f"⚠️ Legacy setup.py found at {legacy.relative_to(ROOT)} — may trigger deprecated install flow")
    else:
        print("✅ No legacy setup.py detected")

def audit_emoji_usage():
    print("🎯 Auditing emoji usage in feedback modules...\n")
    feedback_files = list((PHRED_DIR / "cli" / "utils").glob("*.py"))
    for file in feedback_files:
        content = file.read_text()
        if "print(" in content and "emoji" not in content:
            print(f"⚠️ {file.name}: raw print statements without emoji feedback")
        elif "emoji" in content:
            print(f"✅ {file.name}: emoji feedback detected")
        else:
            print(f"❓ {file.name}: no print or emoji usage found")

def run_all():
    scan_imports()
    check_init_files()
    validate_editable_install()
    check_setup_py_conflict()
    audit_emoji_usage()
    print("\n🏁 Diagnostic complete. Review flagged items above.")

if __name__ == "__main__":
    run_all()
