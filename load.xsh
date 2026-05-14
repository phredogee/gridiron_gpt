# ~/projects/my_project/load.xsh

from datetime import datetime
import os
from xonsh import __xonsh__
env = __xonsh__.env

# 🛡️ Guard against duplicate banners
if '__PROJECT_BANNER_SHOWN__' not in env:
    env['__PROJECT_BANNER_SHOWN__'] = True

    # 🌟 Contributor welcome
    print("🚀 Welcome back to My_Project, phredo! 🌌")

    # 🧠 Optional: sourcing fingerprint
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = env.get("USER", "unknown")
    log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

    try:
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] load.xsh banner shown for {user}\n")
        print(f"📝 Banner sourcing logged → {log_path}")
    except Exception as e:
        print(f"⚠️ Failed to write sourcing log: {e}")
