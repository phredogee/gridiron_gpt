# source_logging.xsh — Contributor trace logging

from datetime import datetime
import os

env = __xonsh__.env

if '__SOURCE_LOGGING_LOADED__' not in env:
    env['__SOURCE_LOGGING_LOADED__'] = '1'

    log_dir = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs")
    log_file = os.path.join(log_dir, "source_log.txt")

    # Ensure log directory exists
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Optional: rotate if log is too large
    if os.path.isfile(log_file) and os.path.getsize(log_file) > 5_000_000:
        os.rename(log_file, log_file + ".bak")

    def log_source_safe(path):
        with open(log_file, "a") as f:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] source_safe → {path}", file=f)

    # Make function globally accessible
    __xonsh__.ctx['log_source_safe'] = log_source_safe

    print("🧾 source_logging.xsh loaded — trace logging active.")
