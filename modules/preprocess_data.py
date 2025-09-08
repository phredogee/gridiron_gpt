# modules/preprocess_data.py

def preprocess_players(raw_data: list) -> list:
    print("🧪 Dry-run: preprocessing player data...")
    """Normalize and clean raw player data."""
    print("🧼 Preprocessing player data...")
    from modules.preprocess_data import preprocess_players

    return [
        {
            "name": player.get("name", "Unknown"),
            "position": player.get("position", "UNK"),
            "total_yards": int(player.get("rushing_yards", 0)) + int(player.get("receiving_yards", 0)),
            "touchdowns": int(player.get("touchdowns", 0))
        }
        for player in raw_data
    ]
