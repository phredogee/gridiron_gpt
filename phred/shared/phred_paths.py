from xonsh import __xonsh__
from phred_utils import print_banner

PHRED_DEBUG = __xonsh__.env.get("PHRED_DEBUG", False)

def dedupe_path(verbose=False):
    if PHRED_DEBUG:
        print("🐛 [DEBUG] Starting PATH deduplication...")

    if __xonsh__.env.get("PHRED_PATH_CLEANED"):
        print("⏭️  Skipping path refresh — already done this session.")
        return

    seen = set()
    new_path = []
    for p in __xonsh__.env["PATH"]:
        if p not in seen:
            seen.add(p)
            new_path.append(p)
    __xonsh__.env["PATH"] = new_path
    __xonsh__.env["PHRED_PATH_CLEANED"] = True

    print("🔄 PATH refreshed:", len(new_path), "entries")
    print("✨ Snap binaries are now discoverable!")
    if verbose or PHRED_DEBUG:
        print("🧪 PATH deduplication: ✅")
