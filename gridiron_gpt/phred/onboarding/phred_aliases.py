# ~/gridiron_gpt/phred_aliases.py

print("🔗 phred_aliases.py loading...")

from phred_utils import print_banner
from xonsh.built_ins import aliases
from xonsh import __xonsh__

PHRED_VERBOSE = __xonsh__.env.get("PHRED_VERBOSE", False)

def register_alias(name, func):
    if name in aliases:
        if PHRED_VERBOSE:
            print(f"⚠️ Alias '{name}' already exists. Skipping.")
        return
    aliases[name] = func
    if PHRED_VERBOSE:
        print(f"✅ Registered alias: {name}")

# 🧪 Example: Toggle debug mode
def toggle_debug():
    env = __xonsh__.env
    env["PHRED_DEBUG"] = not env.get("PHRED_DEBUG", False)
    print(f"🧠 Debug mode: {'On' if env['PHRED_DEBUG'] else 'Off'}")

# 📊 Example: Print phred status
def phred_status():
    env = __xonsh__.env
    print("📊 Phred Status")
    print(f"🔁 Hooks loaded: {env.get('PHRED_HOOKS_LOADED', False)}")
    print(f"🧠 Debug mode: {'On' if env.get('PHRED_DEBUG') else 'Off'}")
    print(f"📣 Verbose mode: {'On' if env.get('PHRED_VERBOSE') else 'Off'}")

# 🏈 Example: Show NFL scores
from gridiron_fetch import gridiron_scores

# 🔗 Register aliases
register_alias("toggle-debug", toggle_debug)
register_alias("phred-status", phred_status)
register_alias("gridiron-scores", gridiron_scores)

print("🔗 phred_aliases.py loaded.")
print_banner("Registering CLI Aliases", emoji="🔗")
