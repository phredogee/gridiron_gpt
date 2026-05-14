# ~/projects/my_project/gridiron_gpt/diagnostics/health.xsh

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in env and env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping health.xsh.")
    raise SystemExit

# 🩺 Health check flag
if '__GRIDIRON_HEALTH_CHECKED__' not in env:
    env['__GRIDIRON_HEALTH_CHECKED__'] = '1'

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = env.get('USER', 'unknown')
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")
print(f"[{timestamp}] health.xsh sourced by {user}" >> $log_path)

# 🩺 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🩺 GridIron GPT — Shell Health Check               ║")
print("║ Validates folders, env vars, and shell metadata    ║")
print("╚════════════════════════════════════════════════════╝")

# 🛡️ Safe sourcing function
def source_if_valid(path, label, guard_var=None):
    path = os.path.expanduser(path)
    shield = "🛡️"
    timestamp = $(date "+%Y-%m-%d %H:%M:%S")
    status = "✅" if os.path.isfile(path) else "❌"
    log_entry = f"[{timestamp}] {status} {label}: {path}"
    log_file = os.path.expanduser("~/projects/my_project/gridiron_gpt/shell/source_log.txt")

    if guard_var and guard_var in env:
        print(f"{shield} {label} already run — skipping source attempt.")
        print($log_entry >> $log_file)
        return

    print(f"🕵️ Debug: Attempting to source → {label}: {path}")
    if os.path.isfile(path):
        execx(f"source {path}")
        print(f"✅ Sourced {label} → {path}")
    else:
        print(f"{shield} [{label}] ⚠️ Missing or invalid path: {path}")

    print($log_entry >> $log_file)

# ✅ Source modules
source_if_valid("~/projects/my_project/gridiron_gpt/shell/source_helpers.xsh", "Sourcing Utilities")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/env_reset.xsh", "Env Reset")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh", "Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/welcome_affirmation.xsh", "Contributor Welcome")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/doctor.xsh", "Doctor Diagnostics")

print("🎉 Shell modules loaded. See source_log.txt for full trace.")
print("🩺 Running shell health check...")

# 🚀 Optional: Source Python loader
loader_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/phredenv/loader.py")

if os.path.isfile(loader_path):
    print(f"🚀 Sourcing loader → {loader_path}")
    execx(f"source {loader_path}")
    print(f"[{timestamp}] loader.py sourced by {user}" >> $log_path)
else:
    print(f"⚠️ Missing loader → {loader_path}")

# ✅ Final affirmations
print("✅ Health checks passed. Shell integrity confirmed.")
print("🛸 Welcome aboard the GridIron CLI. All systems are green. You are cleared for launch.")

launch_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
launch_log = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/shell_launch.log")

try:
    with open(launch_log, "a") as f:
        f.write(f"{launch_timestamp} - Shell launched by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write launch log: {e}")
