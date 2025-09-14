# phred/feedback/context.py
"""

┌────────────────────────────────────────────────────────────┐
│  🧪 phred.feedback.context — FeedbackContext Teach Banner  │
├────────────────────────────────────────────────────────────┤
│ Purpose: Context manager for emoji-rich CLI diagnostics    │
│                                                            │
│ ✅ Class: FeedbackContext                                  │
│   • Wraps CLI output in semantic banners                   │
│   • Supports dry-run debugging and log capture             │
│   • Prints entry/exit lines for visual clarity             │
│                                                            │
│ ✅ Usage Pattern                                           │
│   with FeedbackContext("Starting ESPN fetch", level="info")│
│       print("Inside context")                              │
│                                                            │
│ ✅ Features                                                │
│   • Emoji map for levels: info, success, warning, error    │
│   • Optional dry_run flag for debug labeling               │
│   • `.debug(msg)` method for structured logging            │
│                                                            │
│ ⚠️ Common Pitfalls                                          │
│   • Importing from wrong module (e.g. missing context.py)  │
│   • Forgetting to expose via __init__.py                   │
│   • Overwriting __all__ and hiding FeedbackContext         │
│                                                            │
│ 🛠️ Contributor Tip                                          │
│   • Use FeedbackContext for onboarding banners, dry-run    │
│   • Pair with banner() for consistent CLI output           │
└────────────────────────────────────────────────────────────┘
"""

import logging
from contextlib import ContextDecorator
from modules.utils import EMOJIS

class FeedbackContext:
    def __init__(self, status, dry_run=False):
        self.status = status
        self.dry_run = dry_run
        self.logs = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.logs.append(f"Exception: {exc_value}")

    def log(self, message):
        self.logs.append(message)

    def __str__(self):
        emoji = EMOJIS.get(self.status, "❓")
        return f"{emoji} {' | '.join(self.logs)}"

    def debug(self, msg):
        log_msg = f"{'DRY-RUN ' if self.dry_run else ''}DEBUG: {msg}"
        self.logs.append(log_msg)
        print(log_msg)
        logging.getLogger(__name__).debug(log_msg)

    def render(self):
        return "\n".join(self.logs)
