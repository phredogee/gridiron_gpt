from chinese_zodiac import ZODIAC_TRAITS

def get_zodiac(year: int) -> dict:
    if year < 1900 or year > 2100:
        raise ValueError("Year out of supported range (1900–2100)")

    sign = ZODIAC_SIGNS[(year - 4) % 12]
    element = ELEMENTS[((year - 4) % 10) // 2]
    traits = ZODIAC_TRAITS.get(sign, "🌟 Traits not found.")

    return {"year": year, "sign": sign, "element": element, "traits": traits}

if __name__ == "__main__":
    try:
        year = int(input("Enter your birth year: "))
        zodiac = get_zodiac(year)
        print(zodiac)
    except ValueError as e:
        print(f"❌ {e}")
