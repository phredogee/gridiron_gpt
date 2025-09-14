# phred/cli/utils/feedback.py

from contextlib import contextmanager

def banner(message: str, level: str = "info"):
    emoji_map = {
        "info": "ℹ️",
        "success": "✅",
        "warn": "⚠️",
        "error": "❌",
        "dryrun": "🧪",
    }
    emoji = emoji_map.get(level, "ℹ️")
    print(f"{emoji} {message}")

def success(message: str):
    banner(message, level="success")

def error(message: str):
    banner(f"Error: {message}", level="error")

@contextmanager
def feedback_context(message: str, level: str = "info"):
    print("—" * 40)
    banner(message, level=level)
    yield
    print("—" * 40)
