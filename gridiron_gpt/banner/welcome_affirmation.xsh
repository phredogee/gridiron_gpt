# gridiron_gpt/shell/welcome_affirmation.xsh — Contributor Affirmation Module
import os
from datetime import datetime

# 🛡️ Guard: Prevent duplicate rendering
if '__GRIDIRON_AFFIRMATION_SHOWN__' in env and env['__GRIDIRON_AFFIRMATION_SHOWN__']:
    print("🌟 Contributor affirmations already rendered — skipping.")
else:
    env['__GRIDIRON_AFFIRMATION_SHOWN__'] = '1'

env['GRIDIRON_SESSION_STARTED'] = True

if env.get('GRIDIRON_SESSION_STARTED'):
    print("🛡️ Session already started — skipping.")

if '__WELCOME_LOADED__' not in env:
    env['__WELCOME_LOADED__'] = '1'
    source @(welcome_path)
else:
    print("🧩 welcome_affirmation.xsh already sourced.")

def safe_source(path):
    full_path = os.path.expanduser(path)
    if os.path.isfile(full_path):
        source @(full_path)
        print(f"🧩 Sourced: {full_path}")
    else:
        print(f"⚠️ Missing → {path}")

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
safe_source("~/welcome_affirmation.xsh")
user = $USER if 'USER' in env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", env["HOME"])
with open(log_path, "a") as f:
    f.write(f"[{timestamp}] welcome_affirmation.xsh sourced by {user}\n")

# 🌟 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🌟 GridIron GPT — Contributor Affirmation Module   ║")
print("║ Echoes onboarding affirmations and contributor tips║")
print("╚════════════════════════════════════════════════════╝")

# 💬 Affirmations
print("\n🌟 You are entering a shell built for clarity, mentorship, and modular brilliance.")
print("🧠 Every module you touch is a chance to teach, refine, and empower future contributors.")
print("📘 Your shell logs are clean, your sourcing is safe, and your diagnostics are expressive.")
print("💡 Tip: Use phred-quest to view active contributor quests.")
print("💡 Tip: Run doctor.xsh anytime to check shell health.")
print("🚀 You are cleared for launch. Let’s build something legendary.\n")
