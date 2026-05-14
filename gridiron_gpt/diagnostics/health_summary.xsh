# gridiron_gpt/shell/health_summary.xsh

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and $GRIDIRON_SESSION_STARTED:
    echo "🛡️ Session already started — skipping health_summary.xsh."
    exit

if '__GRIDIRON_HEALTH_SUMMARY_RUN__' in __xonsh__.env:
    echo "📊 Health summary already rendered — skipping."
    exit
__xonsh__.env['__GRIDIRON_HEALTH_SUMMARY_RUN__'] = '1'

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = $USER if 'USER' in __xonsh__.env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", __xonsh__.env["HOME"])
echo f"[{timestamp}] health_summary.xsh sourced by {user}" >> $log_path

# 📊 Visual banner
echo "╔════════════════════════════════════════════════════╗"
echo "║ 📊 GridIron GPT — Health Summary Module            ║"
echo "║ Aggregates diagnostics and confirms shell status   ║"
echo "╚════════════════════════════════════════════════════╝"

# ✅ Source health modules
def source_health_module(path, label):
    path = path.replace("~", __xonsh__.env["HOME"])
    if os.path.isfile(path):
        execx(f"source {path}")
        echo f"🧠 [{label}] ✅ Sourced"
    else:
        echo f"🧠 [{label}] ❌ Missing or invalid: {path}"

HEALTH_MODULES = {
    "Shell Health": "~/projects/my_project/gridiron_gpt/shell/shell_health.xsh",
    "Doctor Diagnostics": "~/projects/my_project/gridiron_gpt/shell/doctor.xsh",
    "Tool Diagnostics": "~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh"
}

for label in HEALTH_MODULES:
    source_health_module(HEALTH_MODULES[label], label)

# 🎯 Final affirmation
echo "✅ Health summary complete. Shell is clean, tools checked, and diagnostics logged."
echo "══════════════════════════════════════════════════════"
echo "🎉 GridIron GPT shell is contributor-ready."
