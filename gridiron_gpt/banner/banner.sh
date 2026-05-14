#!/bin/bash
# banner.sh — Cozy shell banner for GridIron GPT

if [ -z "$GRIDIRON_BANNER_SHOWN" ]; then
  export GRIDIRON_BANNER_SHOWN=1
  echo "🚀 Welcome to GridIron GPT, Phredo!"
  echo "🌌 Your shell is warmed up and ready to launch."
fi
