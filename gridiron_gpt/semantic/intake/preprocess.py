# gridiron_gpt/semantic/intake/preprocess.py

from typing import List, Dict, Union
import pandas as pd
from .fetch import get_raw_player_data as fetch_player_data  # ✅ relative import

def clean_player_data(data: Union[List[Dict], pd.DataFrame]) -> List[Dict]:
    """
    Clean and normalize player data.
    """
    print("🧹 Cleaning player data...")
    if isinstance(data, pd.DataFrame):
        data = data.to_dict(orient="records")

    # Example cleaning: strip whitespace from names
    for player in data:
        player["name"] = player["name"].strip()

    return data
