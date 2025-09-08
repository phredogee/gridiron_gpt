#phredenv/alias_registry.xsh

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🎭 Alias Registry — phredenv/alias_registry.xsh       ┃
# ┃ 🧠 Centralized alias definitions with affirmations    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import datetime

def register_alias(name, command, label=None):
    """Safely register a shell alias with feedback."""
    label = label or name
    timestamp = datetime.datetime.now()

    if name in aliases:
        print(f"🔁 Alias '{name}' already exists — skipping.")
    else:
        aliases[name] = command
        print(f"🎭 Alias set: '{name}' → {command}")
        print(f"🕒 Registered at: {timestamp}")
        print(f"🛡️ Affirmed: {label}")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧭 Default Aliases                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

register_alias('python', 'python3', 'Python Interpreter')
register_alias('greet-contributor', "echo '🛡️ Welcome, noble contributor!'", 'Contributor Greeting')
register_alias('launch-cli', 'python main.py', 'CLI Launcher')
