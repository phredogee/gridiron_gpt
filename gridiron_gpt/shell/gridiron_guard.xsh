# gridiron_gpt/shell/gridiron_guard.xsh — Centralized Guard Logic
from datetime import datetime
import os

# 🧠 Timestamp for logging
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/guard_trace.log")
env["GRIDIRON_GUARD_STATUS"] = "initialized"

# 🛡️ Guard registry
GUARD_FLAGS = {
    "GRIDIRON_SESSION_STARTED": "Session already started — skipping.",
    "__GRIDIRON_BANNER_RENDERED__": "Banner already rendered — skipping.",
    "__GRIDIRON_WELCOME_RENDERED__": "Welcome already rendered — skipping.",
    "__GRIDIRON_AFFIRMATION_SHOWN__": "Affirmations already shown — skipping.",
    "__emoji_palette_sourced__": "Emoji palette already sourced — skipping.",
    "__shell_health_checked__": "Shell health already checked — skipping.",
    "__registry_loaded__": "Registry already loaded — skipping."
}

# 🧼 Guard initializer
def init_guard(flag):
    if flag in env and env[flag]:
        print(f"🛡️ {GUARD_FLAGS.get(flag, 'Already sourced — skipping.')}")
        return False
    env[flag] = True
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] {flag} initialized by {user}\n")
    return True

