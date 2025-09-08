# scripts/reset_session.py

import os
import shutil
from pathlib import Path
import argparse
import platform
import sys
from datetime import datetime

LOG_LINES = []

def log(msg):
    print(msg)
    LOG_LINES.append(msg)

LOG_LINES.append(f"🕒 Reset started at: {datetime.now().strftime('%Y-%m-%d %H:%M %Z')}")
LOG_LINES.append(f"🔧 Python: {sys.version.split()[0]}")
LOG_LINES.append(f"🖥️ OS: {platform.system()} {platform.release()}")
LOG_LINES.append(f"📁 Working dir: {os.getcwd()}")

def write_log(log_path):
    log_dir = Path(log_path).parent
    log_dir.mkdir(parents=True, exist_ok=True)
    with open(log_path, "w") as f:
        f.write("\n".join(LOG_LINES))
    print(f"📝 Log written to {log_path}")

def delete_pycache(root=".", dry_run=False):
    log("🧹 [reset] Removing __pycache__ folders...")
    found = False
    for dirpath, dirnames, _ in os.walk(root):
        for dirname in dirnames:
            if dirname == "__pycache__":
                found = True
                full_path = os.path.join(dirpath, dirname)
                if dry_run:
                    log(f"🧐 Would delete: {full_path}")
                else:
                    shutil.rmtree(full_path)
                    log(f"🗑️ Deleted: {full_path}")
    if not found:
        log("✅ No __pycache__ folders found.")

def delete_temp_data(folder="data/temp", dry_run=False):
    temp_path = Path(folder)
    if temp_path.exists():
        log(f"🧼 [reset] Clearing temp data in {folder}...")
        if dry_run:
            log(f"🧐 Would delete: {folder}")
        else:
            shutil.rmtree(temp_path)
            log(f"🗑️ Deleted: {folder}")
    else:
        log(f"✅ No temp data found at {folder}")

def reset_flags(flag_file="session_flags.json", dry_run=False):
    path = Path(flag_file)
    if path.exists():
        if dry_run:
            log(f"🧐 Would delete: {flag_file}")
        else:
            path.unlink()
            log(f"🚫 [reset] Session flags cleared: {flag_file}")
    else:
        log(f"✅ No session flags to clear.")

def cleanup_module_artifacts(module_name, dry_run=False):
    path = Path(f"modules/{module_name}/artifacts")
    if path.exists():
        log(f"🧹 [reset] Clearing artifacts for module: {module_name}")
        if dry_run:
            log(f"🧐 Would delete: {path}")
        else:
            shutil.rmtree(path)
            log(f"🗑️ Deleted: {path}")
    else:
        log(f"✅ No artifacts found for module: {module_name}")

def parse_args():
    parser = argparse.ArgumentParser(description="Reset GridironGPT session")
    parser.add_argument("--dry-run", action="store_true", help="Preview deletions without executing")
    parser.add_argument("--modules", nargs="*", help="Target specific modules for artifact cleanup")
    parser.add_argument("--log", action="store_true", help="Write reset actions to logs/reset_session.log")
    return parser.parse_args()

def main():
    args = parse_args()
    log("🔄 Resetting GridironGPT session...")
    delete_pycache(dry_run=args.dry_run)
    delete_temp_data(dry_run=args.dry_run)
    reset_flags(dry_run=args.dry_run)

    if args.modules:
        for module in args.modules:
            cleanup_module_artifacts(module, dry_run=args.dry_run)

    log("✅ Session reset complete.")

    if args.log:
        write_log("logs/reset_session.log")

if __name__ == "__main__":
    main()
