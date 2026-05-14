#!/usr/bin/env bash

echo "🚀 Launching test suite..."

# Move to project root
cd "$(dirname "$0")/.." || exit 1

# Set PYTHONPATH to include both my_project and its parent
export PYTHONPATH="$(pwd)/..:$(pwd):$PYTHONPATH"
echo "📦 PYTHONPATH set to: $PYTHONPATH"

# Shell-aware banner
case "$SHELL" in
  */xonsh) echo "🐚 Detected Xonsh shell — activating shell-aware diagnostics..." ;;
  */bash)  echo "🐚 Detected Bash shell — standard activation path." ;;
  */zsh)   echo "🐚 Detected Zsh shell — watch for path quirks." ;;
  *)       echo "⚠️ Unknown shell: $SHELL — results may vary." ;;
esac

# Clean up caches
echo "🧹 Cleaning up old caches..."
find . -type d -name "__pycache__" -exec rm -r {} +
echo "✅ Cache cleared."

# Warn about deprecated plugins
if grep -q "pytest-catchlog" requirements.txt 2>/dev/null; then
  echo "⚠️ Detected deprecated plugin 'pytest-catchlog'. Consider removing it — it's now built into pytest core."
fi

# Import diagnostics
echo "🔍 Checking critical imports..."
python -c "from phred.cli.utils.feedback import banner; print('🧠 phred import check passed.')" || {
  echo "❌ Could not import phred.cli.utils.feedback. Check PYTHONPATH or module layout."
  exit 1
}

# Run tests
echo "🧪 Running tests..."
python -m pytest gridiron_gpt/tests

echo "🎉 Test run complete."
