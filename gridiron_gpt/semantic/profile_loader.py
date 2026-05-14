# semantic/profile_loader.py

def load_bios(source="espn"):
    """
    Load player bios from ESPN or other sources.
    Currently returns mock data for dry-run and testing.
    """
    if source == "espn":
        return [
            {"name": "Justin Jefferson", "team": "MIN", "position": "WR", "age": 24},
            {"name": "Ja'Marr Chase", "team": "CIN", "position": "WR", "age": 23},
            {"name": "CeeDee Lamb", "team": "DAL", "position": "WR", "age": 25},
        ]
    elif source == "mock":
        return [
            {"name": "Mock Player", "team": "FA", "position": "WR", "age": 99}
        ]
    else:
        print(f"⚠️ Unknown source '{source}' — returning empty bios")
        return []
