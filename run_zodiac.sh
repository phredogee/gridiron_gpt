# run_zodiac.sh

#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Activating environment..."
if [ -f "$HOME/phredenv/bin/activate" ]; then
    source "$HOME/phredenv/bin/activate"
else
    echo "❌ Environment not found at ~/phredenv"
    echo "🧪 Tip: Run setup script or recreate environment with \`python -m venv phredenv\`"
    exit 1
fi

echo "🔮 Running zodiac CLI..."
if command -v zodiac >/dev/null 2>&1; then
    zodiac "$@"
else
    echo "⚠️ 'zodiac' command not found."
    echo "📦 Tip: Check if it's installed via setup.py or pyproject.toml entry point."
    echo "🧰 Try running: \`python main_script.py --year 1992\`"
    exit 1
fi

