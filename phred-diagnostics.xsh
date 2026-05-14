# /projects/my_project/phred-diagnostics.xsh
print("╔════════════════════════════════════════════╗")
print("║ 🧪 Phred Diagnostics — Contributor Mode    ║")
print("╚════════════════════════════════════════════╝")

from datetime import datetime
import os
from shutil import which
if "__xonsh__" in globals():
    env = __xonsh__.env
else:
    print("⚠️ __xonsh__ not available — shell not interactive?")
    env = {}  # fallback to avoid crash

# 🛡️ Prevent duplicate diagnostics
if '__PHRED_DIAGNOSTICS_RUN__' not in env:
    env['__PHRED_DIAGNOSTICS_RUN__'] = True
    print("🩺 Running phred diagnostics...")

    # 🧠 Sourcing fingerprint
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = env.get("USER", "unknown")
    log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

    try:
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] phred-diagnostics.xsh run by {user}\n")
    except Exception as e:
        print(f"⚠️ Failed to write sourcing log: {e}")

    # 📦 Virtual environment
    venv = env.get("VIRTUAL_ENV")
    if venv:
        print(f"📦 Virtual environment: {venv}")
    else:
        print("📦 Virtual environment: ❌ Not active")

    # 🔧 Tool checks
    def check_tool(name):
        if which(name):
            print(f"🔧 {name}: ✅ Found")
        else:
            print(f"🔧 {name}: ❌ Missing")

    for tool in ['python3', 'git', 'nvim']:
        check_tool(tool)

    # 🧠 Shell version
    xonsh_version = env.get("XONSH_VERSION", "unknown")
    print(f"🧠 Xonsh version: {xonsh_version}")

    # 🕒 Completion timestamp
    print(f"🕒 Diagnostics completed at: {timestamp}")
else:
    print("🩺 Diagnostics already run — skipping.")

env["PHRED_DIAGNOSTICS_SUMMARY"] = {
    "timestamp": timestamp,
    "user": user,
    "venv": venv or "❌ Not active",
    "tools": {tool: bool(which(tool)) for tool in ['python3', 'git', 'nvim']},
    "xonsh_version": xonsh_version
}
