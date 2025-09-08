# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🩺 GridIron GPT Shell Health Check — phredenv     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from datetime import datetime
import os
import sys

# 🕒 Timestamp
print(f"🕒 Health check sourced at: {datetime.now()}")

# 🧠 Environment Info
print(f"📦 Virtual Environment: {os.environ.get('VIRTUAL_ENV', '❌ Not set')}")
print(f"🐍 Python Version: {sys.version.split()[0]}")
print(f"📁 Current Directory: {os.getcwd()}")

# 🧪 Module Import Check
try:
    import phredcore
    print("✅ phredcore module import: OK")
except ImportError:
    print("❌ phredcore module import: FAILED")

# 🎭 Alias Integrity Check
if 'python' in aliases:
    print(f"🎭 Alias 'python' → {aliases['python']}")
else:
    print("⚠️ Alias 'python' not set")

# 🌌 Contributor Welcome
print("🌌 Welcome, noble contributor. Your shell is affirmed and diagnostics complete.")

# 🎭 Core Alias Check
for alias_name in ['python', 'greet', 'launch-cli']:
    if alias_name in aliases:
        print(f"🎭 Alias '{alias_name}' → {aliases[alias_name]}")
    else:
        print(f"⚠️ Alias '{alias_name}' not set")
