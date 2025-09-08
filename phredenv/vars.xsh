# phredenv/vars.xsh

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 🧭 GridIron GPT — Environment Variables (vars.xsh)    ┃
# ┃ 🛡️ Role: Gold Shield — Herald of Environment Resets   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

if not __xonsh__.env.get("PHRED_ENV_LOADED", False):
    $PHRED_PROJECT_ROOT = "/home/phredo/projects/my_project/gridiron_gpt"
    $PHRED_ENV_LOADED = True
    $PYTHONPATH = $PHRED_PROJECT_ROOT
    $PHRED_ROLE = "Gold Shield — Herald of Environment Resets"

    print("🧭 Environment variables loaded.")
    print(f"📁 Project Root: {PHRED_PROJECT_ROOT}")
    print(f"🛡️ Role Affirmed: {PHRED_ROLE}")
else:
    print("🔁 vars.xsh already sourced — skipping re-init.")
