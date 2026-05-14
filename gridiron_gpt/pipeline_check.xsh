# gridiron_gpt/pipeline_check.xsh — NFL Pipeline Diagnostics Module

import os
from datetime import datetime
env = __xonsh__.env

# 🛡️ Defensive session guard
if env.get("GRIDIRON_SESSION_STARTED"):
    print("🛡️ Session already started — skipping pipeline_check.xsh.")
    return

# 🛡️ Prevent duplicate diagnostics
if env.get("__PIPELINE_CHECK_RUN__"):
    print("🏈 Pipeline diagnostics already run — skipping.")
    return

env["__PIPELINE_CHECK_RUN__"] = True

# 🧠 Sourcing fingerprint
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] pipeline_check.xsh sourced by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write sourcing log: {e}")

# 🏈 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🏈 GridIron GPT — NFL Pipeline Diagnostics Module  ║")
print("║ Validates config, API keys, and data freshness     ║")
print("╚════════════════════════════════════════════════════╝")

# 📁 Check for pipeline config
config_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/config/pipeline_config.json")
if os.path.isfile(config_path):
    print(f"📁 Config file found → {config_path}")
else:
    print(f"⚠️ Config file missing → {config_path}")

# 🔑 Check for API key
if env.get("NFL_API_KEY"):
    print("🔑 NFL API key: ✅ Present")
else:
    print("🔑 NFL API key: ❌ Missing")

# 📊 Check for recent data file
data_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/data/latest_nfl_stats.json")
if os.path.isfile(data_path):
    try:
        file_time = datetime.fromtimestamp(os.path.getmtime(data_path)).strftime("%Y-%m-%d %H:%M:%S")
        print(f"📊 Latest NFL stats file → {data_path}")
        print(f"🕒 Last modified: {file_time}")
    except Exception as e:
        print(f"⚠️ Failed to read file timestamp: {e}")
else:
    print(f"📊 NFL stats file missing → {data_path}")

# 💡 Contributor tips
print("")
print("💡 Tip: Run doctor.xsh to confirm shell health")
print("💡 Tip: Use phred-quest to view active contributor quests")
print("🚀 You are cleared to launch the NFL pipeline diagnostics.")

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] pipeline_check.xsh diagnostics completed\n")
except Exception as e:
    print(f"⚠️ Failed to write completion log: {e}")
