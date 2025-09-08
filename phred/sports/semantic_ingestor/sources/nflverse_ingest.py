# semantic_ingestor/sources/nflverse_ingest.py

import pandas as pd

def fetch_nflverse_data(season: int, position: str = None) -> pd.DataFrame:
    """
    Fetch player stats from nflverse for a given season.
    Optionally filter by position.
    """
    try:
        base_url = f"https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_{season}.csv"
        df = pd.read_csv(base_url)

        if position:
            df = df[df['position'].str.upper() == position.upper()]

        return df

    except Exception as e:
        raise RuntimeError(f"🛑 nflverse ingest failed: {e}")
