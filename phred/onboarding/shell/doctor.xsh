try:
    python -c "import phred"
    echo "📦 Registry: ✅ phred"
except:
    echo "📦 Registry: ❌ phred not found"

pytest --collect-only | grep phred > /dev/null
if $? == 0:
    echo "🧪 Tests:    ✅ discoverable"
else:
    echo "🧪 Tests:    ❌ not found"
