# banner_theme.xsh — Seasonal Banner Rotation 🎨

import random
env = __xonsh__.env

theme = env.get("CURRENT_EMOJI_THEME", "autumn")
emojis = env.get("CURRENT_EMOJIS", "🍁 🧣 🎃 🌰").split()

# 🧠 Define seasonal banner styles
BANNERS = {
    "autumn": [
        "🍁 Welcome to GridIron GPT — Cozy Contributor Mode 🧣",
        "🎃 Shell diagnostics ready — let’s squash bugs like pumpkins 🌰"
    ],
    "winter": [
        "❄️ Welcome to GridIron GPT — Snowy Contributor Mode ⛄",
        "🧤 Bundle up your shell hygiene — it’s cold out there 🎄"
    ],
    "spring": [
        "🌸 Welcome to GridIron GPT — Blooming Contributor Mode 🐣",
        "☔ Let’s clean up your shell like spring rain 🌷"
    ],
    "summer": [
        "🌞 Welcome to GridIron GPT — Sunny Contributor Mode 🕶️",
        "🍉 Refresh your shell setup — it’s hot out there 🏖️"
    ]
}

# 🎨 Select banner
banner_options = BANNERS.get(theme, BANNERS["autumn"])
selected_banner = random.choice(banner_options)

max_width = 50
trimmed = selected_banner[:max_width]
print(f"║ {trimmed:<{max_width}} ║")

# 🖼️ Display banner
print("╔════════════════════════════════════════════════════╗")
print(f" {selected_banner:<50} ║")                          ║")
print("╚════════════════════════════════════════════════════╝")
