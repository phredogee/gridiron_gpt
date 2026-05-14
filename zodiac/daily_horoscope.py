# zodiac/daily_horoscope.py

import requests
import os
API_KEY = os.getenv("CHINESE_HORO_API_KEY", "/api/chinese-horo")

BASE_URL = "https://astrologicalapi.com/docs/1.0/api/chinese-horo"

def fetch_daily_horoscope(sign):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"sign": sign, "day": "today"}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("horoscope", "No horoscope available.")
        except ValueError:
            return "⚠️ Horoscope data is missing or malformed."
    else:
        return f"❌ Error fetching horoscope: {response.status_code}"
