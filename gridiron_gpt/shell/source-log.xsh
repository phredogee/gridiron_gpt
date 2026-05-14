# gridiron_gpt/shell/source-log.xsh — GridIron GPT Shell Source Logger

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping source-log.xsh.")
    raise SystemExit

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
trace_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(trace_path, "a") as f:
    print(f"[{timestamp}] source-log.xsh sourced by {user}", file=f)

# 📜 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 📜 GridIron GPT — Source Logger Module             ║")
print("║ Logs sourcing attempts with timestamps and status  ║")
print("╚════════════════════════════════════════════════════╝")

# 🧠 Source log path
source_log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_log.txt")

# 🧠 Session header (once per session)
if '__SOURCE_LOG_SESSION_HEADER__' not in __xonsh__.env:
    session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(source_log_path, "a") as f:
        print(f"🧠 New session started at: {session_start} by {user}", file=f)
        print("══════════════════════════════════════════════════════", file=f)
    __xonsh__.env['__SOURCE_LOG_SESSION_HEADER__'] = '1'

# 🧠 Safe logging function
def log_source(module_name, path):
    path = os.path.expanduser(path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "✅" if os.path.isfile(path) else "❌"
    log_line = f"[{timestamp}] {status} {module_name} sourced by {user} → {path}"

    if os.path.isfile(path):
        print(f"🔍 Logging: {module_name} → {path}")
    else:
        print(f"⚠️ Cannot log {module_name} — file missing: {path}")

    with open(source_log_path, "a") as f:
        print(log_line, file=f)

# 🧪 Example usage
log_source("banner", "~/projects/my_project/gridiron_gpt/shell/banner.xsh")
log_source("doctor", "~/projects/my_project/gridiron_gpt/shell/doctor.xsh")
log_source("phred-quest", "~/projects/my_project/gridiron_gpt/shell/phred-quest.xsh")
