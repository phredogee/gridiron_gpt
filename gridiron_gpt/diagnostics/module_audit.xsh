# module_audit.xsh — Contributor Shell Hygiene Audit

import os
import shlex 
import subprocess
from datetime import datetime
env = __xonsh__.env
env["AUDIT_COMPLETE"] = datetime.now().isoformat()
env["AUDIT_SUMMARY_TIMESTAMP"] = datetime.now().isoformat()

log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_log.txt")

# 🧼 Write audit header
try:
    with open(log_path, "w") as f:
        f.write("🔍 Running module audit...\n")
        f.write(f"🕒 Audit started at {datetime.now().isoformat()}\n")
except Exception as e:
    print(f"⚠️ Failed to write audit header: {e}")

# 🧩 Updated helper function using shlex
def grep_lines(pattern):
    return subprocess.getoutput(shlex.join(["bash", "-c", pattern])).splitlines()

print()
print("╔════════════════════════════════════════════╗")
print("║ 🧠 GridIron Shell Audit — Contributor Mode ║")
print("╚════════════════════════════════════════════╝")
print()

# 🧠 Audit for deprecated env imports
bad_env_imports = grep_lines("find ~/projects/my_project/gridiron_gpt/ -name '*.xsh' -exec grep -H 'from xonsh.built_ins import env' {} \\;")
with open(log_path, "a") as f:
    f.write("🧠 Checking for deprecated 'env' imports...\n")
    for line in bad_env_imports:
        f.write(f"❌ Deprecated env import: {line}\n")
    f.write(f"🔢 Found {len(bad_env_imports)} deprecated import lines.\n\n")

# 🧠 Audit for unsafe return usage
unsafe_returns = grep_lines("grep -r '^return' ~/projects/my_project/gridiron_gpt/**/*.xsh")
with open(log_path, "a") as f:
    f.write("🧠 Checking for unsafe 'return' usage...\n")
    for line in unsafe_returns:
        f.write(f"⚠️ Unsafe return: {line}\n")
    f.write(f"🔢 Found {len(unsafe_returns)} return statements.\n\n")

# 🧠 Audit for __xonsh__.env usage
xonsh_env_usage = grep_lines("grep -r '__xonsh__.env' ~/projects/my_project/gridiron_gpt/**/*.xsh")
with open(log_path, "a") as f:
    f.write("🧠 Checking for __xonsh__.env usage...\n")
    for line in xonsh_env_usage:
        f.write(f"🔧 Replace with env[]: {line}\n")
    f.write(f"🔢 Found {len(xonsh_env_usage)} usages.\n\n")

# ✅ After line 53 (end of xonsh_env_usage audit)
env["AUDIT_SUMMARY"] = {
    "deprecated_env": len(bad_env_imports),
    "unsafe_returns": len(unsafe_returns),
    "raw_env_usage": len(xonsh_env_usage)
}

# 🧠 Audit session flags
flags = ["BANNER_SHOWN", "EMOJI_ROTATED", "DIAGNOSTICS_RUN"]
with open(log_path, "a") as f:
    f.write("🧠 Session flag summary:\n")
    for flag in flags:
        val = env.get(flag, "❌ Not set")
        f.write(f"🧩 {flag} → {val}\n")
    f.write("\n")

preview = env.get("CURRENT_EMOJIS", "🍁 🧣 🎃 🌰")
with open(log_path, "a") as f:
    f.write(f"🎨 Emoji preview → {preview} at {datetime.now().isoformat()}\n\n")

print("✅ Audit complete. See source_log.txt for results.")

if not bad_env_imports and not unsafe_returns and not xonsh_env_usage:
    print("🎉 All clear! Your shell modules are clean and contributor-ready.")
    print("🧡 Affirmation: Your code teaches through clarity. Keep going!")
