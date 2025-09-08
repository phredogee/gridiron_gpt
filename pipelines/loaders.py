#gpt/pipelines/loaders.py

"""
loaders.py — Loads fantasy football pipeline components:
- CSV data
- Label encoders for position and weather
- Trained decision tree model

Used by CLI tools and shell diagnostics.
"""
import os
import pandas as pd
import joblib

def load_pipeline(
    data_path=os.getenv("FANTASY_DATA_PATH", "fantasy_data.csv"),
    position_encoder_path=os.getenv("POSITION_ENCODER_PATH", "le_position.pkl"),
    weather_encoder_path=os.getenv("WEATHER_ENCODER_PATH", "le_weather.pkl"),
    model_path=os.getenv("MODEL_PATH", "decision_tree_model.pkl")
):
    df = pd.read_csv(data_path)
    le_position = joblib.load(position_encoder_path)
    le_weather = joblib.load(weather_encoder_path)
    model = joblib.load(model_path)
    return df, le_position, le_weather, model

if __name__ == "__main__":
    print("🧪 Running pipeline loader diagnostics...")
    try:
        df, le_position, le_weather, model = load_pipeline()
        print(f"✅ Loaded {len(df)} rows of data.")
        print("✅ Encoders and model loaded successfully.")
    except Exception as e:
        print(f"❌ Loader diagnostics failed: {e}")
