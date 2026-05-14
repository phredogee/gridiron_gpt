#!/usr/bin/env bash
set -e

echo "🔍 Validating test files..."

MISSING=0
for file in tests/test_*.py; do
  if [ ! -f "$file" ]; then
    echo "⚠️ Missing expected test file: $file"
    MISSING=1
  fi
done

if [ "$MISSING" -eq 0 ]; then
  echo "✅ All expected test files are present."
else
  echo "❌ Some test files are missing. Please review."
  exit 1
fi
