# gridiron_gpt/shell/pipeline_diagnostics.xsh — NFL Pipeline Diagnostics Module

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and $GRIDIRON_SESSION_STARTED:
    echo "🛡️ Session already started — skipping pipeline_diagnostics.xsh."
    exit

if '__NFL_DIAGNOSTICS_RUN__' in __xonsh__.env:
    echo "🩺 NFL diagnostics already run — skipping."
    exit
__xonsh__.env['__NFL_DIAGNOSTICS_RUN__'] = '1'

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = $USER if 'USER' in __xonsh__.env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", __xonsh__.env["HOME"])
echo f"[{timestamp}] pipeline_diagnostics.xsh sourced by {user}" >> $log_path

# 🏈 Visual banner
echo "╔════════════════════════════════════════════════════╗"
echo "║ 🏈 GridIron GPT — NFL Pipeline Diagnostics Module  ║"
echo "║ Initializes shell hooks for NFL data pipeline      ║"
echo "║ Future diagnostics will check API status, logs,    ║"
echo "║ and contributor-friendly outputs                   ║"
echo "╚════════════════════════════════════════════════════╝"

echo "🏈 NFL Pipeline Diagnostics Module loaded — no checks defined yet."

# 🕒 Completion timestamp
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
echo f"🕒 Loaded at: {timestamp}"
# 📁 Check for pipeline config
config_path = "~/projects/my_project/gridiron_gpt/config/pipeline_config.json"
config_path = config_path.replace("~", __xonsh__.env["HOME"])
if os.path.isfile(config_path):
    echo f"📁 Config file found → {config_path}"
else:
    echo f"⚠️ Config file missing → {config_path}"

# 🔑 Check for API key
if 'NFL_API_KEY' in __xonsh__.env:
    echo "🔑 NFL API key: ✅ Present"
else:
    echo "🔑 NFL API key: ❌ Missing"

# 📊 Check for recent data file
data_path = "~/projects/my_project/gridiron_gpt/data/latest_nfl_stats.json"
data_path = data_path.replace("~", __xonsh__.env["HOME"])
if os.path.isfile(data_path):
    file_time = $(date -r @data_path "+%Y-%m-%d %H:%M:%S")
    echo f"📊 Latest NFL stats file → {data_path}"
    echo f"🕒 Last modified: {file_time}"
else:
    echo f"📊 NFL stats file missing → {data_path}"

# 💡 Contributor tip
echo ""
echo "💡 Tip: Run doctor.xsh to confirm shell health"
echo "💡 Tip: Use phred-quest to view active contributor quests"
echo ""
