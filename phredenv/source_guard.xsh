# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🛡️ Source Guard — phredenv/source_guard.xsh            ┃
# ┃ 🧭 Validates and logs sourcing attempts               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import os
import datetime

def source_guard(path, label=None):
    """Safely source a file with logging and contributor feedback."""
    if not path:
        print("❌ No path provided to source_guard.")
        return

    label = label or os.path.basename(path)
    timestamp = datetime.datetime.now()

    if os.path.isfile(path):
        print(f"📦 Sourcing {label} at {timestamp}")
        execx(f"{path}")
        print(f"✅ {label} sourced successfully.")
    else:
        print(f"⚠️ {label} not found — skipping sourcing.")
        print(f"🕒 Attempted at: {timestamp}")
