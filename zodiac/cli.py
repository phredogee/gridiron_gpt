# zodiac/cli.py

from chinese_zodiac import get_zodiac
from daily_horoscope import fetch_daily_horoscope
from daily_affirmation import get_affirmation
from fetch_horoscope import get_daily_message

EMOJI_MAP = {
    "Rat": "🐀", "Ox": "🐂", "Tiger": "🐅", "Rabbit": "🐇",
    "Dragon": "🐉", "Snake": "🐍", "Horse": "🐎", "Goat": "🐐",
    "Monkey": "🐒", "Rooster": "🐓", "Dog": "🐕", "Pig": "🐖"
}

def main():
    print("🌟 Welcome to the Chinese Zodiac CLI")
    year = prompt_for_year()
    result = get_zodiac(year)
    emoji = EMOJI_MAP.get(result["sign"], "✨")

    print(f"\n{emoji} Sign: {result['sign']}")
    print(f"🌟 Element: {result['element']}")
    print(f"🧠 You’re a {result['sign']} — known for being {result['traits']}.")

    # Daily content
    horoscope = fetch_daily_horoscope(result["sign"])
    print(f"\n🔮 Daily Horoscope for {result['sign']}:\n{horoscope}")

    affirmation = get_affirmation(result["sign"])
    print(f"\n🌞 Daily Affirmation:\n{affirmation}")

    message = get_daily_message(result["sign"])
    print(f"\n{message}")
    except ValueError as e:
        print(f"❌ Error: {e}")

def fetch_horoscope():
    try:
        response = requests.post("https://aztro.sameerkumar.website?sign=aries&day=today")
        if response.status_code == 200:
            return response.json().get("description")
        else:
            print(f"⚠️ API unavailable (status {response.status_code}), falling back.")
            return None
    except Exception as e:
        print(f"❌ API error: {e}")
        return None

if __name__ == "__main__":
    main()
