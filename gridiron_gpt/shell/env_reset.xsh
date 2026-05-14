# gridiron_gpt/shell/env_reset.xsh — GridIron GPT Environment Reset Module 🔄

env = __xonsh__.env

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in env and env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping env_reset.xsh.")
    raise SystemExit

# 🛡️ Prevent duplicate reset
if '__GRIDIRON_ENV_RESET_RUN__' in env:
    print("🔄 Environment already reset — skipping.")
    raise SystemExit
env['__GRIDIRON_ENV_RESET_RUN__'] = '1'

# 🕒 Timestamp and user
from datetime import datetime
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = env.get('USER', 'unknown')

# 📜 Log sourcing fingerprint
trace_log = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")
env_log = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/env_reset.log")

echo f"[{timestamp}] env_reset.xsh sourced by {user}" >> $trace_log
echo f"[{timestamp}] Environment reset triggered by {user}" >> $env_log

# 🧩 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🔄 GridIron GPT — Environment Reset Module         ║")
print("║ Clears session flags and resets shell state        ║")
print("╚════════════════════════════════════════════════════╝")
print("🔄 Resetting shell environment...")

# 🧹 Clear session flags
flags_to_clear = [
    '__SHELL_HEALTH_CHECK_RUN__',
    '__SHELL_DIAGNOSTICS_RUN__',
    '__GRIDIRON_BANNER_RUN__',
    '__GRIDIRON_SOURCE_HELPERS_RENDERED__',
    '__GRIDIRON_WELCOME_RENDERED__',
    '__GRIDIRON_WELCOME_AFFIRMATION_RUN__',
    '__PHRED_QUEST_RUN__',
    '__PHREDENV_LOADER_RUN__'
]
for flag in flags_to_clear:
    env.pop(flag, None)

# 🧼 Optional: Clear aliases if needed
# aliases.clear()

print("✅ Environment reset complete.")
