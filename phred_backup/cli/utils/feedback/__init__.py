# phred/cli/utils/feedback/__init__.py

from .banner import success

def success(message):
    print(f"✅ {message}")

def warn(message, level="warning"):
    emoji = {
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "❌"
    }.get(level, "⚠️")
    print(f"{emoji} {message}")
