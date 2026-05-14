# zodiac/fetch_horoscope.py

import requests
import json
import os

API_KEY = "your_api_key_here"  # Replace with your actual key
BASE_URL = "https://divineapi.com/horoscope/chinese-horoscope"

def fetch_from_api(sign):
    if not API_KEY or API_KEY == "your_api_key_here":
        return None  # Skip API call if key is missing or placeholder

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            return data.get("horoscope", None)
        else:
            return None
    except Exception:
        return None

def fetch_from_local(sign):
    path = os.path.join(os.path.dirname(__file__), "zodiac_affirmations.json")
    print(f"📁 Loading affirmations from: {path}")  # ✅ Now scoped correctly
    try:
        with open(path, "r", encoding="utf-8") as f:
            affirmations = json.load(f)
        return affirmations.get(sign, "🌙 Trust your instincts today.")
    except Exception as e:
        return f"🚫 Failed to load affirmation: {e}"

def get_daily_message(sign):
    message = fetch_from_api(sign)
    if message:
        return f"🔮 Today’s Horoscope: {message}"
    else:
        fallback = fetch_from_local(sign)
        return f"🌞 Daily Affirmation: {fallback}"

def load_affirmation(path="affirmations.txt"):
    print(f"📁 Loading affirmations from: {path}")
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("⚠️ Affirmation file not found. Using fallback.")
        return "You are radiant and resilient."
