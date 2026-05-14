def normalize_player(raw):
    return {
        "name": raw.get("fullName"),
        "position": raw.get("position", {}).get("name"),
        "team": raw.get("proTeam", {}).get("name"),
        "id": raw.get("id")
    }
