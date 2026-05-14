#gridiron_gpt/ data_pipeline.py

# gridiron_gpt/data_pipeline.py

import pandas as pd

DEFAULT_SEASONS = [2023, 2024]

def get_pbp(seasons: list[int] = None) -> pd.DataFrame:
    import nflreadpy as nfl
    seasons = seasons or DEFAULT_SEASONS
    print(f"📡 Fetching play-by-play data for seasons: {seasons}")
    return nfl.load_pbp(seasons).to_pandas()

def get_player_stats(seasons: list[int] = None) -> pd.DataFrame:
    import nflreadpy as nfl
    seasons = seasons or DEFAULT_SEASONS
    print(f"📊 Fetching player stats for seasons: {seasons}")
    return nfl.load_player_stats(seasons).to_pandas()

def get_team_stats(seasons: list[int] = None) -> pd.DataFrame:
    import nflreadpy as nfl
    seasons = seasons or DEFAULT_SEASONS
    print(f"🏟️ Fetching team stats for seasons: {seasons}")
    return nfl.load_pbp(seasons).to_pandas()

def clean_player_stats(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["player_id", "position"])
    df = df[df["position"].isin(["QB", "RB", "WR", "TE"])]
    return df

# Aliases matching test expectations
load_play_by_play = get_pbp
load_player_stats = get_player_stats
load_team_stats = get_team_stats

if __name__ == "__main__":
    pbp = get_pbp([2022, 2023])
    player_stats = get_player_stats([2022, 2023])
    print(f"✅ Loaded {len(player_stats)} player records and {len(pbp)} plays")
