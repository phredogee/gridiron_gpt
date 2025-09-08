# env.xsh 🌤️
# Shell setup for phred-reset

import datetime
import os
vars_path = "/home/phredo/projects/my_project/gridiron_gpt/phredenv/vars.xsh"
execx(vars_path)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧭 Load core variables                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
execx(f"{PHRED_PROJECT_ROOT}/phredenv/vars.xsh")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🩺 Run health diagnostics                         ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
source_guard(f"{PHRED_PROJECT_ROOT}/phredenv/health.xsh", "health.xsh")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🛡️ Environment Initialization Guard                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
if not __xonsh__.env.get("PHRED_ENV_LOADED", False):
    $PHRED_ENV_LOADED = True
    print("🌱 Environment initialized.")
else:
    print("🔁 Environment already loaded. Skipping.")

vars_path = f"{$PHRED_PROJECT_ROOT}/phredenv/vars.xsh"
