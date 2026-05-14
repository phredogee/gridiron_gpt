# gridiron_gpt/banner/banner.xsh
import os
from datetime import datetime
env = __xonsh__.env

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧭 Banner Setup — GridIron GPT                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Fallback ICONS dictionary for shell context
ICONS = {
    "info": "ℹ️",
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "dryrun": "🧪",
    "debug": "🐞"
}

# Safely assign ICON
ICON = ICONS.get("info", "ℹ️")

# Print banner
print("╔════════════════════════════════════════════════════╗")
print(f" {ICON} GridIron GPT — Banner Module                ║")
print("╚════════════════════════════════════════════════════╝")

# 🧠 Sourcing fingerprint
try:
    timestamp = $(date "+%Y-%m-%d %H:%M:%S")
except Exception:
    timestamp = "unknown"

user = $USER if 'USER' in __xonsh__.env else "unknown"

log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
home_dir = __xonsh__.env["HOME"] if "HOME" in __xonsh__.env else "/home/phredo"
log_path = log_path.replace("~", home_dir)

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] banner.xsh sourced by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write sourcing log → {log_path}")
    print(f"🪛 Error: {e}")

# 🌟 Welcome message
print("🌟 Welcome to GridIron GPT Shell")
print("🧠 CLI v0.1.1 | Registry: ✅ phred | Shell: ✅ phredenv")

# 🕒 Launch time
try:
    launch_time = $(date "+%Y-%m-%d %H:%M:%S")
except Exception:
    launch_time = "unknown"
print(f"🕒 Launch time: {launch_time}")

# 💡 Contributor tip
print("💡 Tip: Use doctor.xsh to check your shell health anytime.")
print("══════════════════════════════════════════════════════")

# Sage Advice from Phred
print("✅ GridIron GPT shell modules loaded. Welcome, contributor!")

# 🛡️ Session guard
if 'GRIDIRON_SESSION_STARTED' not in env:
    env['GRIDIRON_SESSION_STARTED'] = True
else:
    print("🛡️ Session already started — skipping.")

def show_gridiron_banner():
    if '__GRIDIRON_BANNER_SHOWN__' not in env:
        env['__GRIDIRON_BANNER_SHOWN__'] = '1'
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║🌟 Welcome to GridIron GPT Shell"                              ║") 
        print(f"🕒 Launch time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"║")
        print("╚═══════════════════════════════════════════════════════════════╝")

