# gridiron_gpt/shell/phredenv-loader.xsh

# GridIron GPT Python Loader

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping phredenv-loader.xsh.")
    raise SystemExit

# 🛡️ Prevent duplicate loader run
if '__PHREDENV_LOADER_RUN__' in __xonsh__.env:
    print("🚀 phredenv-loader already run — skipping.")
    raise SystemExit

__xonsh__.env['__PHREDENV_LOADER_RUN__'] = '1'

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(log_path, "a") as f:
    print(f"[{timestamp}] phredenv-loader.xsh sourced by {user}", file=f)

# 🚀 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🚀 GridIron GPT — Phredenv Python Loader           ║")
print("║ Launches Python-side logic for shell onboarding    ║")
print("╚════════════════════════════════════════════════════╝")

# 🧠 Launch Python loader
loader_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/phredenv/loader.py")

if os.path.isfile(loader_path):
    print(f"🚀 Launching loader → {loader_path}")
    python3 $loader_path
    with open(log_path, "a") as f:
        print(f"[{timestamp}] loader.py launch attempted by {user}", file=f)
else:
    print(f"⚠️ loader_path missing or invalid: {loader_path}")
    with open(log_path, "a") as f:
        print(f"[{timestamp}] loader.py missing — launch skipped by {user}", file=f)
