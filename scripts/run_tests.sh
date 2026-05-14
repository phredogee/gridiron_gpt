#!/usr/bin/env bash

echo "🚀 Launching test suite..."

# Move to project root
cd "$(dirname "$0")/.." || exit 1

# Set PYTHONPATH
export PYTHONPATH=$(pwd)
echo "📦 PYTHONPATH set to: $PYTHONPATH"

# Clean up caches
echo "🧹 Cleaning up old caches..."
find . -type d -name "__pycache__" -exec rm -r {} +
echo "✅ Cache cleared."

# Run tests
echo "🧪 Running tests..."
python -m pytest gridiron_gpt/tests

echo "🎉 Test run complete."
