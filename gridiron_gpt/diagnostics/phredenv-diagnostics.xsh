# gridiron_gpt/shell/phredenv-diagnostics.xsh

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and $GRIDIRON_SESSION_STARTED:
    echo "🛡️ Session already started — skipping phredenv-diagnostics.xsh."
    exit

if '__PHREDENV_DIAGNOSTICS_RUN__' in __xonsh__.env:
    echo "🧪 Phredenv diagnostics already sourced — skipping."
    exit
__xonsh__.env['__PHREDENV_DIAGNOSTICS_RUN__'] = '1'

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = $USER if 'USER' in __xonsh__.env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", __xonsh__.env["HOME"])
echo f"[{timestamp}] phredenv-diagnostics.xsh sourced by {user}" >> $log_path

# 🧪 Visual banner
echo "╔════════════════════════════════════════════════════╗"
echo "║ 🧪 GridIron GPT — Phredenv Diagnostics Loader      ║"
echo "║ Sourcing shell health, doctor, and tool checks     ║"
echo "╚════════════════════════════════════════════════════╝"

# 🧠 Source diagnostics modules
source_if_valid("~/projects/my_project/gridiron_gpt/shell/doctor.xsh", "Doctor Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh", "Tool Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/shell_health.xsh", "Shell Health")

# 🎯 Final affirmation
echo "✅ Phredenv diagnostics sourced. Shell health modules are active."
