# phredenv/semantic/profile_builder.py

def build_player_profile(raw: dict, dry_run: bool = False) -> dict:
    """
    Build a player profile from raw stats.
    In dry_run mode, return predictable tags for testing.
    """
    tags = []

    # Simple QB tagging logic
    if raw.get("position") in ("QB", "Quarterback"):
        if raw.get("passing_yards", 0) > 4000 and raw.get("touchdowns", 0) >= 30:
            tags.append("elite")
        tags.append("starter")

    profile = {
        "name": raw.get("name"),
        "team": raw.get("team"),
        "position": raw.get("position"),
        "stats": raw,
        "tags": tags
    }

    return profile
