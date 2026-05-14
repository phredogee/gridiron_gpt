# affirm.xsh — Seasonal Contributor Affirmations 🌈

import random
env = __xonsh__.env

theme = env.get("CURRENT_EMOJI_THEME", "autumn")
emojis = env.get("CURRENT_EMOJIS", "🍁 🧣 🎃 🌰").split()

# 💬 Seasonal affirmations
AFFIRMATIONS = {
    "autumn": [
        "🍁 Your clarity helps others fall into place.",
        "🧣 You wrap contributors in warmth and wisdom.",
        "🎃 You squash bugs like pumpkins—brilliant and bold!"
    ],
    "winter": [
        "❄️ Your code is crystalline—sharp and beautiful.",
        "⛄ You build snowball momentum with every fix.",
        "🧤 You bundle contributors in clarity and care."
    ],
    "spring": [
        "🌸 You help ideas bloom with every commit.",
        "🐣 You nurture new contributors with patience.",
        "☔ You clean up code like spring rain—gentle and thorough."
    ],
    "summer": [
        "🌞 You shine through complexity with warmth.",
        "🍉 You refresh the shell with juicy insights.",
        "🏖️ You make onboarding feel like a day at the beach."
    ]
}

# 💬 Select affirmation
affirm_options = AFFIRMATIONS.get(theme, AFFIRMATIONS["autumn"])
selected_affirmation = random.choice(affirm_options)

# 🌈 Display affirmation
print()
print("╔════════════════════════════════════════════════════╗")
print(f"║ {selected_affirmation:<50} ║")
print("╚════════════════════════════════════════════════════╝")
print()
