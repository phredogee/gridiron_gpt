# gridiron_gpt/emoji/emoji_rotation.py — Seasonal Emoji Rotation 🌀

import random
import os
env = __xonsh__.env

# 🧠 Define emoji cohorts
EMOJI_COHORTS = {
    "autumn": ["🍁", "🧣", "🎃", "🌰"],
    "winter": ["❄️", "⛄", "🎄", "🧤"],
    "spring": ["🌸", "🐣", "🌷", "☔"],
    "summer": ["🌞", "🏖️", "🍉", "🕶️"]
}

# 🎨 Select theme from env or random fallback
def select_emoji_theme():
    theme = os.environ.get("EMOJI_THEME")
    if theme not in EMOJI_COHORTS:
        theme = random.choice(list(EMOJI_COHORTS.keys()))
    return theme

CURRENT_THEME = select_emoji_theme()
CURRENT_EMOJIS = EMOJI_COHORTS[CURRENT_THEME]

# 🌈 Expose to shell environment
env["CURRENT_EMOJI_THEME"] = CURRENT_THEME
env["CURRENT_EMOJIS"] = " ".join(CURRENT_EMOJIS)

# 🔄 Rotate emojis without repetition
def rotate_emojis(container, used=None):
    if used is None:
        used = set()
    fresh = [e for e in container if e not in used]
    if not fresh:
        used.clear()
        fresh = container[:]
    selected = random.choice(fresh)
    used.add(selected)
    print(f"🔄 Rotating from {container}, used: {used}, selected: {selected}")
    return selected

# 🧪 Example rotation (can be removed in production)
if __name__ == "__main__":
    used_emojis = set()
    for _ in range(5):
        rotate_emojis(CURRENT_EMOJIS, used_emojis)
