# gridiron_gpt/shell/phred-shell-launch.xsh — GridIron GPT Shell Launcher

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping phred-shell-launch.xsh.")
    raise SystemExit

if '__PHRED_SHELL_LAUNCH_RUN__' in __xonsh__.env:
    print("🛡️ phred-shell-launch already run — skipping.")
    raise SystemExit

__xonsh__.env['__PHRED_SHELL_LAUNCH_RUN__'] = '1'

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(log_path, "a") as f:
    print(f"[{timestamp}] phred-shell-launch.xsh sourced by {user}", file=f)

# 🚀 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🚀 GridIron GPT — Phred Shell Launcher             ║")
print("║ Safely sources shell modules and logs diagnostics  ║")
print("╚════════════════════════════════════════════════════╝")

# ✅ Safe sourcing function
def source_if_valid(path, label):
    path = os.path.expanduser(path)
    success = os.path.isfile(path)
    shield = "🛡️"

    if success:
        execx(f"source {path}")
        print(f"🔍 Sourcing attempt: {label} → {path}")
    else:
        print(f"{shield} [{label}] ⚠️ Missing or invalid path: {path}")

    log_source_attempt(path, label, success)

# 🧠 Logging function
def log_source_attempt(path, label, success):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "✅" if success else "❌"
    log_line = f"[{timestamp}] {status} {label}: {path}"
    log_file = os.path.expanduser("~/projects/my_project/gridiron_gpt/shell/source_log.txt")
    with open(log_file, "a") as f:
        print(log_line, file=f)

# ✅ Define sourcing paths
SHELL_PATHS = {
    "Shell Health": "~/projects/my_project/gridiron_gpt/shell/shell_health.xsh",
    "Source Helpers": "~/projects/my_project/gridiron_gpt/shell/source_helpers.xsh"
}

print(f"🧭 SHELL_PATHS initialized with {len(SHELL_PATHS)} entries")

# 🚀 Source each module
for label in SHELL_PATHS:
    source_if_valid(SHELL_PATHS[label], label)

print("🎉 Shell launch complete. All systems sourced and logged.")
print("══════════════════════════════════════════════════════")
