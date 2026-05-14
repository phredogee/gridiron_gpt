# gridiron_gpt/shell/phred-aliases.xsh — Contributor Alias Registry

import os
from datetime import datetime
env = __xonsh__.env

# 🛡️ Defensive session guard
if env.get("GRIDIRON_SESSION_STARTED"):
    print("🛡️ Session already started — skipping.")
    raise SystemExit

env["GRIDIRON_SESSION_STARTED"] = True

# 🧠 Sourcing fingerprint
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

try:
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] phred-aliases.xsh sourced by {user}\n")
except Exception as e:
    print(f"⚠️ Failed to write sourcing log: {e}")

# 🧵 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🧵 GridIron GPT — Alias Registry Module            ║")
print("║ Defines contributor-friendly shell shortcuts       ║")
print("╚════════════════════════════════════════════════════╝")

# 🧠 Core aliases
aliases['python'] = 'python3'
aliases['gc'] = 'git commit -m'
aliases['refresh-shell'] = 'source ~/.xonshrc'

aliases['phred-reset'] = lambda: source_safe(os.path.expanduser("~/projects/my_project/gridiron_gpt/phredenv/reset.xsh"))
aliases['source-safe'] = lambda: source_safe(os.path.expanduser("~/projects/my_project/gridiron_gpt/shell/source_helpers.xsh"))
aliases['phred-diagnostics'] = lambda: source_safe(os.path.expanduser("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh"))

print("✅ Aliases registered: python, gc, refresh-shell, phred-reset, source-safe")

# 🧠 Project Shell Aliases
aliases['audit'] = 'source ~/projects/my_project/gridiron_gpt/diagnostics/module_audit.xsh'

# 🕒 Completion timestamp
print(f"🕒 Alias registry loaded at: {timestamp}")
