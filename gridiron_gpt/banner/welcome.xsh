# gridiron_gpt/shell/welcome.xsh — GridIron GPT Contributor Welcome Module
import os
from datetime import datetime

# 🛡️ Defensive session guard
if env.get('GRIDIRON_SESSION_STARTED'):
    print("🛡️ Session already started — skipping.")

if env.get('GRIDIRON_SESSION_STARTED'):
    print("🛡️ Session already started — skipping module.")

env['__GRIDIRON_WELCOME_RENDERED__'] = '1'

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = $USER if 'USER' in env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", env["HOME"])
with open(log_path, "a") as f:
    f.write(f"[{timestamp}] welcome.xsh sourced by {user}\n")

# 🌟 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🌟 GridIron GPT — Contributor Welcome Module       ║")
print("║ Greets contributors and confirms shell readiness   ║")
print("╚════════════════════════════════════════════════════╝")

# 🕒 Timestamp and path
cwd = $PWD

# 🌟 Welcome banner
print("\n🌟 Welcome to GridIron GPT")
print(f"👋 Hello, {user} — your shell is live and ready.")
print("🧠 CLI Version: v0.1.1")
print("📦 Registry: ✅ phred")
print("🧪 Tests:    ✅ discoverable")
print(f"🩺 Shell:    ✅ phredenv (xonsh {XONSH_VERSION})")
print(f"🧭 Path:     {cwd}")
print(f"🕒 Launched at: {timestamp}")

# 💡 Tips
print("📘 Tip: Type phred-reset to reload your environment.")
print("📂 Tip: Use ls gridiron_gpt/shell to explore shell tools.")
print("💡 Tip: Run python main.py to launch the CLI.")

print("\n🚀 Let's build something legendary.")
