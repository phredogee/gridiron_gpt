# phredenv_loader.xsh
# 🛠️ Defensive sourcing and environment initialization for phredenv

import os
from datetime import datetime
env = __xonsh__.env

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🛡️ Define source-safe loader                       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def source_safe(path):
    if os.path.isfile(path):
        try:
            execx(f"source {path}")
            print(f"📦 Sourced → {path}")
        except Exception as e:
            print(f"❌ Failed to source {path}: {e}")
    else:
        print(f"⚠️ Missing file → {path}")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 📁 Define project root                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
PROJECT_ROOT = os.path.expanduser("~/projects/my_project/gridiron_gpt")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 📦 Source core modules                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
source_safe(f"{PROJECT_ROOT}/banner/banner.xsh")
source_safe(f"{PROJECT_ROOT}/emoji/emoji_palette.xsh")
source_safe(f"{PROJECT_ROOT}/diagnostics/diagnostics.xsh")
source_safe(f"{PROJECT_ROOT}/env/phredenv-status.xsh")
source_safe(f"{PROJECT_ROOT}/shell/shell_health.xsh")
source_safe(f"{PROJECT_ROOT}/shell/pipeline_diagnostics.xsh")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧠 Defensive sourcing with affirmation            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
if '__phredenv_status_sourced__' not in env:
    env['__phredenv_status_sourced__'] = True
    source_safe(f"{PROJECT_ROOT}/env/phredenv-status.xsh")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🌱 Environment Initialization                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
if '__PHREDENV_LOADED__' not in env:
    env['__PHREDENV_LOADED__'] = True
    print("🔧 phredenv loader sourced")

    # Set GRIDIRON_MODE if not already defined
    env['GRIDIRON_MODE'] = env.get('GRIDIRON_MODE', 'dev')
    print(f"🧪 GRIDIRON_MODE set to: {env['GRIDIRON_MODE']}")

    # Optional: sourcing fingerprint
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = env.get("USER", "unknown")
    log_path = os.path.join(env["HOME"], "projects/my_project/gridiron_gpt/logs/source_trace.log")

    try:
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] phredenv_loader.xsh sourced by {user}\n")
        print(f"📝 Sourcing fingerprint logged → {log_path}")
    except Exception as e:
        print(f"⚠️ Failed to write sourcing log: {e}")
