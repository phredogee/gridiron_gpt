# emoji.xsh — Seasonal emoji rotation and contributor affirmations

# 🧼 Session hygiene guard
if '__emoji_loaded__' not in locals():
    __emoji_loaded__ = True

# 🌸 Define seasonal emoji themes
__EMOJI_THEMES__ = {
    "winter": ["❄️", "☃️", "🧣"],
    "spring": ["🌸", "🐣", "🌱"],
    "summer": ["☀️", "🏖️", "🍉"],
    "autumn": ["🍂", "🎃", "🧥"]
}

# 🧠 Emoji rotation logic
def get_seasonal_emojis():
    from datetime import datetime
    month = datetime.now().month
    try:
        if month in [12, 1, 2]:
            return __EMOJI_THEMES__["winter"]
        elif month in [3, 4, 5]:
            return __EMOJI_THEMES__["spring"]
        elif month in [6, 7, 8]:
            return __EMOJI_THEMES__["summer"]
        elif month in [9, 10, 11]:
            return __EMOJI_THEMES__["autumn"]
    except KeyError:
        return ["✨", "🌟", "💫"]

def rotate_seasonal_emoji():
    from random import choice
    global __EMOJI_USED__
    if '__EMOJI_USED__' not in globals():
        __EMOJI_USED__ = set()
    emojis = get_seasonal_emojis()
    fresh = [e for e in emojis if e not in __EMOJI_USED__]
    if not fresh:
        __EMOJI_USED__.clear()
        fresh = emojis[:]
    selected = choice(fresh)
    __EMOJI_USED__.add(selected)
    print(f"🔄 Rotated seasonal emoji → {selected}")
    return selected

# 🔁 Run once per session
if not env.get("EMOJI_ROTATED", False):
    rotate_seasonal_emoji()
    env["EMOJI_ROTATED"] = True
    env["EMOJI_ROTATION_STATUS"] = "done"
