# phred/shared/cli_base.py
import functools

def emoji_feedback(level="info"):
    emoji_map = {
        "info": "ℹ️",
        "warn": "⚠️",
        "error": "❌",
        "success": "✅"
    }
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{emoji_map.get(level, 'ℹ️')} Running {func.__name__}...")
            return func(*args, **kwargs)
        return wrapper
    return decorator
