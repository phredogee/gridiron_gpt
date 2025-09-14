# gridiron_gpt/semantic/intake/fetch.py
from typing import Union, List, Dict
# from phred.sports.espn import fetch_from_espn
import pandas as pd

def get_raw_player_data(source: str = "local") -> Union[List[Dict], pd.DataFrame]:
    """
    Fetch raw player data from a source.

    Parameters
    ----------
    source : str
        Options: 'local', 'api', 'scrape', 'espn'

    Returns
    -------
    list[dict] or pd.DataFrame
        Player data in a consistent structure.
    """
    print(f"📡 Fetching player data from source: {source!r}...")

    if source == "local":
        data = [{"name": "Patrick Mahomes", "team": "KC", "position": "QB"}]

    elif source == "api":
        # TODO: call your API client here
        data = [{"name": "Jalen Hurts", "team": "PHI", "position": "QB"}]

    elif source == "scrape":
        # TODO: scraping logic here
        data = [{"name": "Justin Jefferson", "team": "MIN", "position": "WR"}]

    elif source == "espn":
        from phred.sports.espn import fetch_from_espn  # lazy import to avoid circulars
        data = fetch_from_espn(dry_run=True)["players"]

    else:
        raise ValueError(f"Unknown source: {source}")

    return data
