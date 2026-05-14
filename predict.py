# predict.py

import argparse
from project_gridiron_gpt.pipeline import load_pipeline, SemanticPipeline
from project_gridiron_gpt.interface.cli import run_prediction_cli

def main():
    parser = argparse.ArgumentParser(description="Fantasy prediction CLI")
    parser.add_argument("--position", required=True, help="Player position (e.g., WR, RB)")
    parser.add_argument("--weather", required=True, help="Weather condition (e.g., sunny, rainy)")
    args = parser.parse_args()

    # Load pipeline
    df, le_pos, le_weather, model = load_pipeline()
    pipeline = SemanticPipeline(df, le_pos, le_weather, model)

    # Run prediction
    try:
        result = pipeline.predict(args.position, args.weather)
        print(f"Prediction for {args.position} in {args.weather}: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_prediction_cli()
