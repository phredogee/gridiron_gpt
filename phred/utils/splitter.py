# phred/utils/splitter.py

def split_matchup(matchup: str):
    """
    Split a matchup string into two team names.

    Example:
        "Team A vs Team B" -> ("Team A", "Team B")
    """
    if not isinstance(matchup, str):
        raise ValueError("matchup must be a string")

    # Normalize spacing and split on 'vs' (case-insensitive)
    parts = matchup.split(" vs ")
    if len(parts) != 2:
        parts = matchup.split(" VS ")
    if len(parts) != 2:
        parts = matchup.split(" Vs ")

    if len(parts) != 2:
        raise ValueError(f"Invalid matchup format: {matchup}")

    home, away = parts[0].strip(), parts[1].strip()
    return home, away
