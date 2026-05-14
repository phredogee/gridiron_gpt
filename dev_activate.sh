#!/usr/bin/env bash
# dev_activate.sh — Shell-aware onboarding script

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$PROJECT_ROOT:$PYTHONPATH"

echo "📦 PYTHONPATH set to: $PROJECT_ROOT"

# Confirm import source
IMPORT_PATH=$(python -c "import phred; print(phred.__file__)")
echo "✅ phred import succeeded from: $IMPORT_PATH"

# Optional: run banner check if available
python -c "from phred.cli.utils.feedback import banner; print('🧠 Import check passed.')"
