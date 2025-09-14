# phredenv/semantic/profile_builder.py

def build_player_profile(raw, dry_run=False):
    """
    Builds a player profile dict from raw stats.
    Adds tags like 'elite' and 'starter' based on simple rules.
    """
    profile = dict(raw)  # copy the raw data
    tags = []

    # Simple tagging logic for test pass
    if raw.get("position") and raw.get("team"):
        tags.append("starter")
    if raw.get("touchdowns", 0) >= 30 or raw.get("passing_yards", 0) >= 4000:
        tags.append("elite")

    profile["tags"] = tags
    return profile
