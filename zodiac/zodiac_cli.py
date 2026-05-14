# 🧭 Contributor Note:
# This script uses interactive prompts to engage users.
# Input is validated with emoji-tiered feedback.
# Future enhancement: add lunar calendar support or personality traits per sign.

import argparse
import sys
from zodiac.chinese_zodiac import get_chinese_zodiac, get_zodiac_traits

def zodiac(year: int):
    sign = get_chinese_zodiac(year)
    traits = get_zodiac_traits(sign)
    print(f"\n🎉 Based on the year {year}, your Chinese Zodiac sign is: 🐾 {sign} 🐾")
    print(f"✨ Traits of the {sign}: {traits}")

def prompt_for_birth_year():
    print("🎋 Welcome to the Chinese Zodiac Finder!")
    print("🧧 Let's discover your Zodiac sign based on your birth year.")

    while True:
        user_input = input("📅 Please enter your 4-digit birth year (e.g. 1992): ")
        if not user_input.isdigit():
            print("⚠️ That doesn't look like a number. Try again.")
            continue

        year = int(user_input)
        if year < 1000 or year > 9999:
            print("🚫 That’s not a valid 4-digit year. Please enter a year between 1000 and 9999.")
            continue

        return year

def run_cli():
    parser = argparse.ArgumentParser(
        description="🧧 Find the Chinese Zodiac sign for a 4-digit birth year."
    )
    parser.add_argument("--year", type=int, help="📅 Birth year (e.g. 1992)")
    parser.add_argument("--test", action="store_true", help="🧪 Run built-in zodiac tests")
    args = parser.parse_args()

    if args.test:
        test_zodiac()
        test_traits()
        sys.exit()

    year = args.year if args.year else prompt_for_birth_year()
    zodiac(year)
    print("✨ May your sign bring you wisdom, strength, and good fortune!")

def test_traits():
    assert get_zodiac_traits("Dragon").startswith("Ambitious")
    assert get_zodiac_traits("Rat").startswith("Quick-witted")
    print("✅ Trait tests passed.")

def test_zodiac():
    assert get_chinese_zodiac(2025) == "Snake"
    assert get_chinese_zodiac(2000) == "Dragon"
    assert get_chinese_zodiac(1996) == "Rat"
    print("✅ Zodiac sign tests passed.")

if __name__ == "__main__":
    run_cli()
