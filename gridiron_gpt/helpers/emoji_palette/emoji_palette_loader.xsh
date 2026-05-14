# emoji_palette_loader.xsh — Seasonal emoji palette sourcing

from datetime import datetime
import os

env = __xonsh__.env
month = datetime.now().month

season = (
    "winter" if month in [12, 1, 2] else
    "spring" if month in [3, 4, 5] else
    "summer" if month in [6, 7, 8] else
    "fall"
)

palette_path = f"~/.xonshrc.d/helpers/emoji_palette/emoji_palette_{season}.xsh"
expanded_path = os.path.expanduser(palette_path)

if os.path.isfile(expanded_path):
    source @(expanded_path)
    print(f"🍁 Seasonal emoji palette loaded → {season.capitalize()}")
else:
    print(f"⚠️ Missing seasonal emoji palette → {season}")
