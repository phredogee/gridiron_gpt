#  modules/pipeline.py

from modules.fetch_raw_data import fetch_player_data
from modules.preprocess_data import preprocess_players
from modules.store_index import store_data
from modules.embed_data import embed_players  # optional

def run_pipeline(embed=False):
    print("🏈 Starting Gridiron GPT pipeline...")

    # Step 1: Fetch raw data
    raw_data = fetch_player_data()
    print(f"📥 Fetched {len(raw_data)} players")

    # Step 2: Preprocess
    clean_data = preprocess_players(raw_data)
    print(f"🧼 Preprocessed data for {len(clean_data)} players")

    # Step 3: Store
    store_data(clean_data)
    print("💾 Data stored successfully")

    # Step 4: Embed (optional)
    if embed:
        embed_players(clean_data)
        print("🧠 Player data embedded")

    print("✅ Pipeline complete.")

def load_pipeline():
    # Load your dataframe
    df = pd.read_csv("your_data.csv")

    # Label encoders
    le_position = LabelEncoder().fit(df["position"])
    le_weather = LabelEncoder().fit(df["weather"])
    le_team = LabelEncoder().fit(df["team"])
    le_opp_team = LabelEncoder().fit(df["opponent_team"])

    # Encode features and train model
    # (Make sure your training includes team and opponent_team)

    return df, le_position, le_weather, le_team, le_opp_team, model
