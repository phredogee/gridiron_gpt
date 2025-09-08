# semantic_ingestor/normalizers/profile_mapper.py

from normalizers.profile_mapper import map_nflverse_profile

def map_nflverse_profile(df) -> list[dict]:
    """Convert nflverse DataFrame into semantic player profiles."""
    profiles = []
    for _, row in df.iterrows():
        profiles.append({
            "name": row.get("player_name"),
            "team": row.get("team"),
            "position": row.get("position"),
            "source": "nflverse",
            "metrics": {
                "passing_yards": row.get("passing_yards"),
                "rushing_yards": row.get("rushing_yards"),
                "receiving_yards": row.get("receiving_yards"),
                "fantasy_points": row.get("fantasy_points"),
            }
        })

def map_to_semantic_profile(df, source: str) -> list[dict]:
    """Convert ESPN DataFrame into semantic player profiles."""
    profiles = []
    for _, row in df.iterrows():
        profiles.append({
            "name": row.get("Player"),
            "team": row.get("Team"),
            "position": row.get("Pos"),
            "source": source,
            "metrics": {
                "rank": row.get("Rank"),
                "points": row.get("Points"),
            }
        })
    return profiles
