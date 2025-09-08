# profiles.py

def format_profile(row):
    """
    Converts a player's stats row into a semantic string for embedding.
    Example: "Patrick Mahomes is a quarterback with 4500 passing yards and 38 touchdowns in 2023."
    """
    name = row.get("Name", "Unknown Player")
    position = row.get("Position", "Unknown Position")
    team = row.get("Team", "Unknown Team")
    stats = f"{row.get('PassingYards', 0)} passing yards and {row.get('Touchdowns', 0)} touchdowns"
    year = row.get("Season", "Unknown Season")
    
    return f"{name} is a {position} for the {team} with {stats} in {year}."

def generate_profiles(df):
    return [format_profile(row) for _, row in df.iterrows()]
