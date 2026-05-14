# zodiac/daily_affirmation.py

import json
import os

def get_affirmation(sign):
    path = os.path.join(os.path.dirname(__file__), "data", "zodiac_affirmations.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            affirmations = json.load(f)
        return affirmations.get(sign, "🌙 Trust your instincts today.")
    except Exception as e:
        return f"⚠️ Could not load affirmation: {e}"

if not os.path.exists(path):
    return "⚠️ Affirmation file not found. Make sure 'data/zodiac_affirmations.json' exists."

if __name__ == "__main__":
    for sign in ["Rat", "Dragon", "Goat", "Phoenix"]:
        print(f"{sign}: {get_affirmation(sign)}")
