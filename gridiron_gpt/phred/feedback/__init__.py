# phred/feedback/__init__.py

"""
┌────────────────────────────────────────────────────────────┐
│  📦 phred.feedback.__init__.py — Export Map & Teach Banner │
├────────────────────────────────────────────────────────────┤
│ Purpose: Centralized export hub for feedback utilities     │
│                                                            │
│ ✅ Imports                                                 │
│   • banner → emoji-rich message printer                    │
│   • success / warning / error → semantic wrappers          │
│   • FeedbackContext → context manager for diagnostics      │
│   • generate_feedback → feedback logic engine              │
│                                                            │
│ ✅ Public API (__all__)                                    │
│   • Exposes key symbols for CLI and test modules           │
│   • Prevents import drift and duplicate definitions        │
│                                                            │
│ ⚠️ Common Pitfalls                                          │
│   • Duplicate __all__ declarations → overwrite exports     │
│   • Importing from nonexistent submodules (e.g. banner.py) │
│   • Defining symbols locally but importing from elsewhere  │
│                                                            │
│ 🛠️ Contributor Tip                                          │
│   • Keep __init__.py lean—delegate logic to submodules     │
│   • Use grep to audit symbol usage across CLI/test suite   │
└────────────────────────────────────────────────────────────┘
"""
# ✅ Never import a symbol from the module you're currently initializing
# ✅ Define shared constants like EMOJIS at the top level
# ✅ Use __all__ to expose them cleanly for CLI and test modules
# 🚫 Don’t re-import from self—Python will throw a circular import error
# Re-export FeedbackContext from context.py for CLI and test integration

import logging
from contextlib import ContextDecorator
from semantic.utils.feedback import success, warning, error
from .banner import render_banner
from .context import FeedbackContext
from .core import generate_feedback

EMOJIS = {
    "info": "ℹ️",
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "dryrun": "🧪",
    "debug": "🐞"
}

__all__ = [
    "render_banner",
    "FeedbackContext",
    "generate_feedback",
    "banner", "banner_info", "banner_warn",
    "success", "warning", "error",
    "EMOJIS"
]

def banner_info(message: str):
    return banner(message, emoji="ℹ️")

def banner_warn(message: str):
    return banner(message, emoji="⚠️")

# Patchable logger for tests
logger = logging.getLogger(__name__)

def banner(message: str,
           status: str = "info",
           level: str = None,
           emoji: str = None) -> str:
    """
    Print and return a banner message with an icon based on status/level.
    Falls back to info icon for unknown statuses.
    Allows overriding the icon with a custom emoji.
    """
    key = (level or status or "info").lower()
    icon = emoji or EMOJIS.get(key, "ℹ️")
    output = f"{icon} {message}"
    print(output)
    return output

def success(message: str):
    return banner(message, status="success")


def warning(message: str):
    return banner(message, status="warning")


def error(message: str):
    return banner(message, status="error")

class FeedbackContext(ContextDecorator):
    ICONS = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌",
        "dryrun": "🧪",
        "debug": "🐞"
    }

    def __init__(self, message, level="info", dry_run=False):
        self.message = message
        self.level = level
        self.dry_run = dry_run
        self.logs = []

    def __enter__(self):
        icon = self.ICONS.get(self.level, "ℹ️")
        print(f"{icon} {self.message}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("—" * 40)
        return False  # don't suppress exceptions

    def debug(self, msg):
        if self.dry_run:
            log_msg = f"DRY-RUN DEBUG: {msg}"
        else:
            log_msg = f"DEBUG: {msg}"
        self.logs.append(log_msg)
        print(log_msg)
        logger.debug(log_msg)


def feedback_context(message, level="info", dry_run=False):
    """
    Return a FeedbackContext for use in 'with' statements.
    """
    return FeedbackContext(message, level=level, dry_run=dry_run)
    icon = EMOJIS.get(self.level, "ℹ️")
