# phred_aliases.xsh
echo "🛠️ Available commands: reset, gridiron, scout, etc."

def reset_gridiron():
    echo "🔄 Running GridironGPT reset..."
    python ./scripts/reset_session.py --log

aliases['reset'] = reset_gridiron
