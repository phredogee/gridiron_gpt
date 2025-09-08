# gridiron_gpt/__main__.py
from interface.cli import main
from .pipeline import load_pipeline, SemanticPipeline

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--position", required=True)
    parser.add_argument("--weather", required=True)
    args = parser.parse_args()

    df, le_pos, le_weather, model = load_pipeline()
    pipeline = SemanticPipeline(df, le_pos, le_weather, model)
    result = pipeline.predict(args.position, args.weather)
    print(f"Prediction for {args.position} in {args.weather}: {result}")

from cli.main import app

if __name__ == "__main__":
    app()
