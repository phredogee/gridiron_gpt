#!/usr/bin/env bash
set -e

echo "🧼 Cleaning up stale Python artifacts..."

find . -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

echo "✅ Pycache and .pyc files removed."
