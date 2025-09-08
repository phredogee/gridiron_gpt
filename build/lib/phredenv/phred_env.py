# ~/phredenv/phred_env.py

PHRED_DEBUG = __xonsh__.env.get("PHRED_DEBUG", False)

def dedupe_path(verbose=False, dry_run=False):
    seen = set()
    new_path = []
    for p in __xonsh__.env["PATH"]:
        if p not in seen:
            seen.add(p)
            new_path.append(p)
    if dry_run:
        print("🔍 Would set PATH to:", new_path)
    else:
        __xonsh__.env["PATH"] = new_path
        if verbose or PHRED_DEBUG:
            print("🧼 PATH deduplicated.")

from path_utils import dedupe_path

dedupe_path()
