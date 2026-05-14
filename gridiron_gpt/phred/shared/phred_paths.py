from phred_utils import print_banner

PHRED_DEBUG = __xonsh__.env.get("PHRED_DEBUG", False)

def dedupe_path(verbose=False):
    if PHRED_DEBUG:
        print("🐛 [DEBUG] Starting PATH deduplication...")

if env.get("PHRED_PATH_CLEANED"):
    ...
for p in env["PATH"]:
    ...
env["PATH"] = new_path
env["PHRED_PATH_CLEANED"] = True

    seen = set() new_path = [] for p in __xonsh__.env["PATH"]:
        if p not in seen:
            seen.add(p)
            new_path.append(p)
    __xonsh__.env["PATH"] = new_path
    __xonsh__.env["PHRED_PATH_CLEANED"] = True

    print("🔄 PATH refreshed:", len(new_path), "entries")
    print("✨ Snap binaries are now discoverable!")
    if verbose or PHRED_DEBUG:
        print("🧪 PATH deduplication: ✅")

if "__xonsh__" in globals():
    env = __xonsh__.env
else:
    print("⚠️ __xonsh__ not available — shell not interactive?")
    env = {}  # fallback to avoid crash

env["PHRED_PATH_CLEANED_AT"] = datetime.now().isoformat()
