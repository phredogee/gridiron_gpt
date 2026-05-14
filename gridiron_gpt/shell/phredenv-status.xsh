# gridiron_gpt/shell/phredenv-status.xsh

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping phredenv-status.xsh.")
    raise SystemExit

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
log_path = os.path.join(__xonsh__.env["HOME"], "projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(log_path, "a") as f:
    print(f"[{timestamp}] phredenv-status.xsh sourced by {user}", file=f)

# 📊 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 📊 GridIron GPT — Shell Status Module              ║")
print("║ Displays virtualenv, shell version, and directory  ║")
print("╚════════════════════════════════════════════════════╝")

# 📦 Virtual environment
venv = __xonsh__.env.get("VIRTUAL_ENV", None)
print(f"📦 Virtualenv: {venv if venv else '❌ Not active'}")

# 🧠 Shell version
version = __xonsh__.env.get("XONSH_VERSION", None)
print(f"🧠 Shell: Xonsh {version if version else '❌ Unknown'}")

# 📁 Current directory
print(f"📁 Current directory: {__xonsh__.env.get('PWD', '❌ Unknown')}")

# 🧩 Optional: Session flags
print(f"🧩 GRIDIRON_MODE: {__xonsh__.env.get('GRIDIRON_MODE', '❌ Not set')}")
print(f"🧩 PHREDENV_LOADED: {__xonsh__.env.get('__PHREDENV_LOADED__', '❌ Not set')}")
print(f"🧩 PIPELINE_CHECK_RUN: {__xonsh__.env.get('__PIPELINE_CHECK_RUN__', '❌ Not set')}")

# 🌟 Optional: Seasonal emoji preview
if 'rotate_seasonal_emoji' in globals():
    print(f"🌟 Seasonal emoji: {rotate_seasonal_emoji()}")
