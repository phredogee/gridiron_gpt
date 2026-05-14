# gridiron_gpt/feedback/__init__.py

def banner(message: str, width: int = 80, emoji: str = "🔔"):
    print("\n" + "═" * width)
    print(f"{emoji} {message}")
    print("═" * width + "\n")

def banner_info(message: str):
    return banner(message, emoji="ℹ️")

def banner_warn(message: str):
    return banner(message, emoji="⚠️")

def success(message: str):
    banner(f"✅ {message}", emoji="✅")

def warning(message: str):
    banner(f"⚠️ {message}", emoji="⚠️")

def error(message: str):
    banner(f"❌ {message}", emoji="❌")

__all__ = ["banner", "banner_info", "banner_warn", "success", "warning", "error"]
