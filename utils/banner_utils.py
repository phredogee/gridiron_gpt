# /gridiron_gpt/utils/banner_utils.py

# 🔧 Remove sys.path hacks if possible—prefer relative imports or proper packaging
# If absolutely needed for dev, wrap in a conditional to avoid polluting sys.path in production
import sys, os
if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath("/home/phredo/projects/my_project/gridiron_gpt"))

# 🧼 Avoid importing functions that are redefined below—this causes confusion and overrides
# from phred.utils.banner_utils import banner, success_banner, warn_banner, fail_banner  # ← Remove

# 🎯 Centralized banner printer with type-based emoji and formatting
def print_banner(text: str, level: str = "info") -> None:
    emojis = {
        "info": "🔍",
        "success": "✅",
        "warn": "⚠️",
        "error": "❌"
    }
    headers = {
        "info": "=" * 40,
        "success": "-" * 40,
        "warn": "-" * 40,
        "error": "-" * 40
    }
    emoji = emojis.get(level, "ℹ️")
    header = headers.get(level, "-" * 40)
    print(f"\n{emoji} {text}\n{header}")

# 🧪 Semantic audit feedback examples
if __name__ == "__main__":
    print_banner("Starting semantic audit", level="info")
    print_banner("All imports resolved", level="success")
    print_banner("ESPN pipeline missing dry-run flag", level="warn")
    print_banner("Schedule validation failed: duplicate matchups", level="error")
