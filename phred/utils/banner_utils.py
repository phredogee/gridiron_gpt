# phred/utils/banner_utils.py

# FeedbackContext has been moved to phred/feedback/context.py
# This module now only handles banner rendering

from contextlib import ContextDecorator

def banner(message: str, level: str = "info") -> str:
    """
    Print and return a banner message with an icon based on the level.
    """
    icons = {
        "info": "ℹ️",
        "success": "✅",
        "warn": "⚠️",
        "error": "❌",
        "dryrun": "🧪",
        "debug": "🐞"
    }
    icon = icons.get(level, "ℹ️")
    output = f"{icon} {message}"
    print(output)
    return output
