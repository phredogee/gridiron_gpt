# gridiron_gpt/diagnostics/diagnostics.xsh — GridIron GPT Diagnostics Module

from xonsh.tools import which
from datetime import datetime
import os
import subprocess
env = __xonsh__.env

# 🛡️ Defensive session guard
if env.get("GRIDIRON_SESSION_STARTED"):
    print("🛡️ Session already started — skipping diagnostics.xsh.")
    exit()

# 🛡️ Prevent duplicate diagnostics
if env.get("__GRIDIRON_DIAGNOSTICS_RUN__"):
    print("🧠 Diagnostics already run — skipping.")
    exit()

env["__GRIDIRON_DIAGNOSTICS_RUN__"] = True

# 🧠 Sourcing fingerprint
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] diagnostics.xsh sourced by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write sourcing log: {e}")

# 🎃 Emoji rotation
try:
    emoji = subprocess.run(
        ["python", "-c", "from emoji_rotation import rotate_emojis; print(rotate_emojis(['🎃','👻','🕸️']))"],
        capture_output=True, text=True
    ).stdout.strip()
    print(f"{emoji} Diagnostics loaded!")
except Exception as e:
    emoji = "🩺"
    print(f"⚠️ Emoji rotation failed: {e}")

# 🩺 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🩺 GridIron GPT — Diagnostics Module               ║")
print("║ Logs shell health, sourcing order, and env state   ║")
print("╚════════════════════════════════════════════════════╝")

# 🧪 Tool checks
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

# 📦 Virtual Environment Check
venv = env.get("VIRTUAL_ENV")
PHREDENV_ACTIVE = bool(venv)

if PHREDENV_ACTIVE:
    print(f"📦 Virtual environment: {venv}")
    print("🧪 Environment confirmed — diagnostics can proceed.")
else:
    print("📦 Virtual environment: ❌ Not active")
    print("⚠️ Environment not active — contributors may need to run setup.")

# 🕒 Completion timestamp
completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🕒 Diagnostics completed at: {completion_time}")
print("══════════════════════════════════════════════════════")
print(f"{emoji} Welcome to your shell session!")
