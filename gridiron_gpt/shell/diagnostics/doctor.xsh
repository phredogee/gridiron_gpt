# gridiron_gpt/shell/doctor.xsh — GridIron GPT Diagnostics Module

import os
from shutil import which
from datetime import datetime
env = __xonsh__.env

# 🛡️ Defensive session guard
if env.get("GRIDIRON_SESSION_STARTED"):
    print("🛡️ Session already started — skipping doctor.xsh.")
    raise SystemExit

# 🛡️ Prevent duplicate diagnostics
if "__SHELL_DIAGNOSTICS_RUN__" in env:
    print("🩺 Diagnostics already run — skipping.")
    raise SystemExit

env["__SHELL_DIAGNOSTICS_RUN__"] = "1"

# 🧠 Sourcing fingerprint
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] doctor.xsh sourced by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write sourcing log: {e}")

# 🧪 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🧪 GridIron GPT — Doctor Diagnostics Module        ║")
print("║ Runs one-time shell diagnostics and confirms env   ║")
print("╚════════════════════════════════════════════════════╝")

print("🕵️ Entering doctor.xsh")
print("🩺 Running shell diagnostics...")

# 📦 Virtual environment status
venv = env.get("VIRTUAL_ENV")
if venv:
    print(f"📦 Virtual environment: {venv}")
else:
    print("📦 Virtual environment: ❌ Not active")

# 📁 Current working directory
print(f"📁 Current directory: {os.getcwd()}")

# 🔧 Tool checks
def check_tool(name):
    if which(name):
        print(f"🔧 {name}: ✅ Found")
    else:
        print(f"🔧 {name}: ❌ Missing")

for tool in ["python3", "git", "nvim"]:
    check_tool(tool)

# 🧠 Shell version
xonsh_version = env.get("XONSH_VERSION", "unknown")
print(f"🧠 Xonsh version: {xonsh_version}")

# 🕒 Completion timestamp
launch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🕒 Diagnostics completed at: {launch_time}")
print("══════════════════════════════════════════════════════")
