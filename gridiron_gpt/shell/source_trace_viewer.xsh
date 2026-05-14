# source_trace_viewer.xsh — Contributor Sourcing History Viewer 📖

import os

log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

def show_trace_log():
    if not os.path.isfile(log_path):
        print("⚠️ No sourcing log found. Run diagnostics or launch shell to generate one.")
        return
    print("📖 GridIron Sourcing History")
    print("══════════════════════════════════════════════════════")
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                print(f"🕒 {line}")
    print("══════════════════════════════════════════════════════")
    print("✅ End of sourcing log.")

show_trace_log()
