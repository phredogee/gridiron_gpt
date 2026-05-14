# env.xsh 🌤️
# Shell setup for phred-reset and environment initialization
# ~/.xonshrc.d/env.xsh
import os
from datetime import datetime
env = __xonsh__.env

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧭 Define project root with fallback              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
if 'PHRED_PROJECT_ROOT' not in env:
    env['PHRED_PROJECT_ROOT'] = os.path.expanduser("~/projects/my_project/gridiron_gpt")

project_root = env['PHRED_PROJECT_ROOT']

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 📦 Load core variables                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
vars_path = f"{project_root}/phredenv/vars.xsh"
if os.path.isfile(vars_path):
    try:
        execx(f"source {vars_path}")
        echo f"📦 Loaded vars.xsh → {vars_path}"
    except Exception as e:
        echo f"⚠️ Failed to source vars.xsh → {vars_path}"
        echo f"🪛 Error: {e}"
else:
    echo f"⚠️ Missing vars.xsh → {vars_path}"

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🩺 Run health diagnostics                         ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
health_path = f"{project_root}/phredenv/health.xsh"
if os.path.isfile(health_path):
    try:
        execx(f"source {health_path}")
        echo f"🩺 Health diagnostics sourced → {health_path}"
    except Exception as e:
        echo f"⚠️ Failed to source health.xsh → {health_path}"
        echo f"🪛 Error: {e}"
else:
    echo f"⚠️ Missing health.xsh → {health_path}"

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🛡️ Environment Initialization Guard              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
if 'PHRED_ENV_LOADED' not in env:
    env['PHRED_ENV_LOADED'] = True
    echo "🌱 Environment initialized."
else:
    echo "🔁 Environment already loaded. Skipping."
