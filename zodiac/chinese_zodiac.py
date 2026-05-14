# zodiac/chinese_zodiac.py

def get_chinese_zodiac(year: int) -> str:
    zodiac_animals = [
        "Monkey",  # 0
        "Rooster", # 1
        "Dog",     # 2
        "Pig",     # 3
        "Rat",     # 4
        "Ox",      # 5
        "Tiger",   # 6
        "Rabbit",  # 7
        "Dragon",  # 8
        "Snake",   # 9
        "Horse",   # 10
        "Sheep"    # 11
    ]
    index = year % 12
    return zodiac_animals[index]

ZODIAC_TRAITS = {
    "Rat": "Quick-witted, resourceful, and adaptable. Rats thrive in dynamic environments.",
    "Ox": "Strong, reliable, and grounded. Oxen are known for their quiet determination.",
    "Tiger": "Brave, competitive, and confident. Tigers lead with passion and boldness.",
    "Rabbit": "Gentle, elegant, and alert. Rabbits bring peace and kindness to those around them.",
    "Dragon": "Ambitious, charismatic, and intelligent. Dragons are natural leaders.",
    "Snake": "Wise, mysterious, and intuitive. Snakes excel in strategy and subtlety.",
    "Horse": "Energetic, independent, and free-spirited. Horses chase adventure.",
    "Sheep": "Compassionate, artistic, and calm. Sheep nurture harmony and creativity.",
    "Monkey": "Clever, curious, and playful. Monkeys bring joy and innovation.",
    "Rooster": "Hardworking, observant, and confident. Roosters shine with precision.",
    "Dog": "Loyal, honest, and protective. Dogs are devoted companions.",
    "Pig": "Generous, sincere, and easygoing. Pigs radiate warmth and abundance."
}

def get_zodiac(year):
    signs = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    ]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    
    sign_index = (year - 4) % 12
    element_index = ((year - 4) % 10) // 2
    
    sign = signs[sign_index]
    element = elements[element_index]
    traits = ZODIAC_TRAITS[sign]
    
    return {
        "sign": sign,
        "element": element,
        "traits": traits
    }

def get_zodiac_traits(sign: str) -> str:
    return ZODIAC_TRAITS.get(sign, "🌟 Traits not found — this sign is still a mystery!")

if __name__ == "__main__":
    while True:
        try:
            year = int(input("🔮 Enter your birth year: "))
            result = get_zodiac(year)
            print(f"\n🎋 The Chinese Zodiac sign for {year} is: {result['sign']}")
            print(f"🌊 Element: {result['element']}")
            print(f"✨ Traits: {result['traits']}")
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter a numeric year like 1992.")
