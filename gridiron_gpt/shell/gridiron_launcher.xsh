# gridiron_gpt/shell/gridiron_launcher.xsh

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping gridiron_launcher.xsh.")
    raise SystemExit

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(log_path, "a") as f:
    print(f"[{timestamp}] gridiron_launcher.xsh sourced by {user}", file=f)

# 🚀 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🚀 GridIron GPT — Launcher Module                  ║")
print("║ Orchestrates shell onboarding and diagnostics      ║")
print("╚════════════════════════════════════════════════════╝")

# 🛡️ Persistent lock file guard
lock_path = os.path.expanduser("~/.gridiron_launcher.lock")

if os.path.isfile(lock_path) or '__GRIDIRON_LAUNCHER_RUN__' in __xonsh__.env:
    print("🛡️ GridIron launcher already initialized — skipping.")
    raise SystemExit

with open(lock_path, "w") as f:
    f.write("locked")

__xonsh__.env['__GRIDIRON_LAUNCHER_RUN__'] = '1'

# 🧩 Source session flags
source /home/phredo/projects/my_project/gridiron_gpt/shell/session_flags.xsh

# 🧩 Source modules
source /home/phredo/projects/my_project/gridiron_gpt/shell/source_helpers.xsh
source /home/phredo/projects/my_project/gridiron_gpt/shell/shell_health.xsh
source /home/phredo/projects/my_project/gridiron_gpt/shell/banner.xsh

# 📦 Log sourced modules
with open(log_path, "a") as f:
    print(f"[{timestamp}] source_helpers.xsh sourced", file=f)
    print(f"[{timestamp}] shell_health.xsh sourced", file=f)
    print(f"[{timestamp}] banner.xsh sourced", file=f)

# ✅ Set session flag after successful sourcing
__xonsh__.env['GRIDIRON_SESSION_STARTED'] = True

# 📁 Check required directories
required_dirs = [
    "~/projects/my_project/gridiron_gpt/shell",
    "~/phredenv"
]

# 🩺 Prevent duplicate health check
if '__SHELL_HEALTH_CHECK_RUN__' in __xonsh__.env:
    print("🩺 Shell health check already run — skipping.")
    raise SystemExit

__xonsh__.env['__SHELL_HEALTH_CHECK_RUN__'] = '1'
print("🩺 Running shell health check...")

# ✅ Check for key folders
for d in required_dirs:
    path = os.path.expanduser(d)
    if os.path.isdir(path):
        print(f"📁 {path}: ✅ Present")
    else:
        print(f"⚠️ {path}: ❌ Missing or inaccessible")

# 🔗 Check for environment variables
env_vars = ['VIRTUAL_ENV', 'PYTHONPATH']

for var in env_vars:
    if var in __xonsh__.env:
        print(f"🔗 {var}: ✅ {__xonsh__.env[var]}")
    else:
        print(f"🔗 {var}: ❌ Not set")

# 🧠 Optional: Check shell type
xonsh_version = __xonsh__.env.get('XONSH_VERSION', 'Unknown')
print("🎯 Shell health check complete. All systems logged and verified.")
print(f"🧠 Shell: Xonsh {xonsh_version}")
print("══════════════════════════════════════════════════════")
