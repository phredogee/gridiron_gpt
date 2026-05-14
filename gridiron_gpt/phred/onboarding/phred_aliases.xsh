# phred_aliases.xsh — Contributor Alias Registry

import os

if "__xonsh__" in globals():
    env = __xonsh__.env
else:
    print("⚠️ __xonsh__ not available — shell not interactive?")
    env = {}  # fallback to avoid crash

env['GRIDIRON_SESSION_STARTED'] = True

if env.get('GRIDIRON_SESSION_STARTED'):
    print("🛡️ Session already started — skipping.")

print("🛠️ Registering contributor aliases...")

# 🔄 Reset alias
def reset_gridiron():
    print("🔄 Running GridironGPT reset...")
    python ./scripts/reset_session.py --log

aliases['reset'] = reset_gridiron

# 🧪 Diagnostics alias
def run_diag():
    diag_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/pipeline_diagnostics.xsh")
    if os.path.isfile(diag_path):
        source(diag_path)
        if 'run_pipeline_diagnostics' in globals():
            run_pipeline_diagnostics()
        else:
            print("⚠️ Diagnostics function not defined")
    else:
        print(f"⚠️ Missing diagnostics file → {diag_path}")

aliases['gridiron'] = run_diag

# 🕵️ Scout alias (placeholder)
def scout_mode():
    print("🕵️ Entering scout mode... (coming soon)")

aliases['scout'] = scout_mode

# 📘 Contributor tips
print("🧩 Aliases registered: reset, gridiron, scout")
print("💡 Tip: Run 'reset' to restart session")
print("💡 Tip: Run 'gridiron' to launch diagnostics")
print("💡 Tip: Run 'scout' to preview contributor tools")
