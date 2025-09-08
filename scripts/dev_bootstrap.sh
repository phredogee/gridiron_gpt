#!/usr/bin/env bash

echo "🚀 Dev bootstrap initialized"

PHRED_PATH="$(pwd)/phred"
export PYTHONPATH="$PHRED_PATH${PYTHONPATH:+:$PYTHONPATH}"
export MY_ENV="dev"

echo "✅ PYTHONPATH set to: $PYTHONPATH"
echo "📦 Project root: $(pwd)"
echo "🚀 Environment mode: $MY_ENV"
