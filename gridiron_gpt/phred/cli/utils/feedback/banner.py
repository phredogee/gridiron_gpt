# phred/cli/utils/feedback/banner.py

# 🧪 Onboarding Tip:
# ✅ Use `render_banner()` to wrap CLI feedback in visual framing
# ✅ Emojis make messages memorable and affirming
# ✅ Centralize formatting logic to keep CLI clean and consistent

def banner_info(message: str):
    print(f"🧠 {message}")

def banner_warn(message: str):
    print(f"🚫 {message}")

def banner_success(message: str):
    print(f"✅ {message}")

def render_banner(message: str, emoji: str = "🧪", width: int = 60) -> str:
    """
    Render a visual banner around a message for CLI feedback.

    Args:
        message (str): The message to display.
        emoji (str): Emoji prefix for visual emphasis.
        width (int): Total banner width.

    Returns:
        str: Formatted banner string.
    """
    border = f"{emoji} " + "-" * (width - 2)
    padded = f"{emoji} {message}".ljust(width)
    return f"\n{border}\n{padded}\n{border}\n"
