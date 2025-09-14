# phred/feedback/banner.py

def render_banner(status, message):
    emoji = EMOJIS.get(status, "ℹ️")  # ✅ use EMOJIS, not STATUS_EMOJI
    if not message:
        message = "No message provided"
    return f"{emoji} {message}"
