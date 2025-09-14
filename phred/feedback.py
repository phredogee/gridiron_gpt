# gridiron_gpt/phred/feedback.py

# ┌────────────────────────────────────────────┐
# │ FeedbackContext vs feedback_context        │
# ├────────────┬───────────────────────────────┤
# │ Class      │ Testable, loggable, reusable  │
# │ Decorator  │ Lightweight, dry-run aware    │
# └────────────┴───────────────────────────────┘

import logging
from contextlib import contextmanager
from modules.utils import EMOJIS

logger = logging.getLogger(__name__)

EMOJIS = {
    "info": "ℹ️",
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "debug": "🛠️"
}

def render_banner(status, message):
    emoji = EMOJIS.get(status, "❓")  # ✅ not STATUS_EMOJI
    if not message:
        message = "No message provided"
    return f"{emoji} {message}"

def banner(message: str, status: str = "info", emoji: str = None) -> str:
    """
    Return a banner string with an emoji and a 40-char ASCII border.
    Empty messages get a placeholder so it's not just the emoji.
    """
    icon = emoji or EMOJIS.get(status, "🔔")
    text = message.strip() or "[no message]"
    border = "-" * 40
    return f"{icon} {text}\n{border}"

@contextmanager
def feedback_context(message: str, level: str = "info", dry_run: bool = False):
    """
    Print a banner on entry and a closing border on exit.
    In dry-run mode, suppress body output and log instead.
    """
    icon = EMOJIS.get(level, "🔔")
    border = "-" * 40
    print(f"{icon} {message}")
    print(border)
    if dry_run:
        logger.info(f"Dry run: {message}")
        yield  # suppress body output
    else:
        try:
            yield
        finally:
            print(border)

render_banner = banner
