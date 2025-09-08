#!/usr/bin/env bash
set -e

echo "👋 Welcome, contributor! Let's clean up and validate your test setup."

bash scripts/clean_tests.sh
bash scripts/validate_tests.sh
bash scripts/run_tests.sh

echo "🌈 You're all set. Happy contributing!"
