
echo "🚀 Dev bootstrap initialized"

$PHRED_PATH = f"{$(pwd)}/phred"

# Safely flatten and normalize existing PYTHONPATH
$EXISTING_PATHS = []
for p in ${...}.get("PYTHONPATH", []):
    if isinstance(p, (str, bytes)):
        $EXISTING_PATHS.append(p)
    elif hasattr(p, '__fspath__'):
        $EXISTING_PATHS.append(str(p))
    else:
        echo f"⚠️ Skipping invalid PYTHONPATH entry: {p}"

# Now assign clean list
$PYTHONPATH = [$PHRED_PATH] + $EXISTING_PATHS

echo f"✅ PYTHONPATH set to: {$PYTHONPATH}"
echo f"🧠 Shell: {$XONSH_VERSION}"
echo f"📦 Project root: {$(pwd)}"
echo f"🚀 Environment mode: {$MY_ENV}"
