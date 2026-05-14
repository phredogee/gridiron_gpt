#gridiron_gpt/ data_pipeline.py

# gridiron_gpt/data_pipeline.py

import nflreadpy as nfl
import pandas as pd
from datetime import datetime
with open("logs/pipeline.log", "a") as f:
    f.write(f"[{datetime.now()}] Loaded NFL data for seasons: {seasons}\n")

def get_pbp(seasons: list[int]) -> pd.DataFrame:
    print(f"📡 Fetching play-by-play data for seasons: {seasons}")
    return nfl.load_pbp(seasons).to_pandas()

def get_player_stats(seasons: list[int]) -> pd.DataFrame:
    print(f"📊 Fetching player stats for seasons: {seasons}")
    return nfl.load_player_stats(seasons).to_pandas()

def clean_player_stats(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["player_id", "position"])
    df = df[df["position"].isin(["QB", "RB", "WR", "TE"])]
    return df

    export NFLREADPY_CACHE=filesystem
    export NFLREADPY_CACHE_DIR=~/projects/my_project/gridiron_gpt/cache

if __name__ == "__main__":
    pbp = get_pbp([2022, 2023])
    player_stats = get_player_stats([2022, 2023])
    print(f"✅ Loaded {len(player_stats)} player records and {len(pbp)} plays")
