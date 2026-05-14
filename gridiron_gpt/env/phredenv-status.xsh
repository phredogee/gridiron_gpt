# env/phredenv-status.xsh

# 📦 phredenv Status Module — Contributor Affirmation
echo "📦 phredenv status sourced — environment confirmed."

# 🛡️ Defensive Guard
if not $__phredenv_status_sourced__:
    $__phredenv_status_sourced__ = True

    # 🧠 Environment Diagnostics
    if $VIRTUAL_ENV:
        echo f"🧼 Virtual environment active → {$VIRTUAL_ENV}"
    else:
        echo "⚠️ No virtual environment detected — contributors may need to activate one."

    # 🔧 Shell Health Summary
    echo "🔧 Shell: Xonsh {$XONSH_VERSION}"
    echo f"🔧 Python: {$(which python3)}"
    echo f"🔧 Git: {$(which git)}"
    echo f"🔧 nvim: {$(which nvim)}"

    # 🧪 Export for downstream modules
    export PHREDENV_ACTIVE = True
    export PHREDENV_PATH = $VIRTUAL_ENV if $VIRTUAL_ENV else "none"
