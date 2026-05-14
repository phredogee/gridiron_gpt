# Move to project root
cd "$(dirname "$0")/.." || exit 1

# Set PYTHONPATH to include parent of my_project
export PYTHONPATH=$(pwd)/..:$PYTHONPATH
echo "📦 PYTHONPATH set to: $PYTHONPATH"
