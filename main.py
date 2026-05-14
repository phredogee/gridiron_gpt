# main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # ✅ Add path before imports

import argparse
from modules.pipeline import load_pipeline
from modules.predictor import predict_action
from gridiron_gpt.pipeline import SemanticPipeline
from zodiac.chinese_zodiac import get_chinese_zodiac, get_zodiac_traits

def prompt_if_missing(args, parser):
    def ask(prompt, cast=str, choices=None):
        while True:
            val = input(prompt)
            try:
                val = cast(val)
                if choices and val not in choices:
                    raise ValueError
                return val
            except ValueError:
                print(f"❌ Invalid input. Expected one of: {choices}" if choices else "❌ Try again.")

    if args.position is None:
        args.position = ask("📌 Enter player position (RB, WR, QB): ", str, ["RB", "WR", "QB"])
    if args.defense_rank is None:
        args.defense_rank = ask("🛡️ Enter opponent defense rank (1–32): ", int)
    if args.weather is None:
        args.weather = ask("🌦️ Enter weather condition (clear, rainy, cloudy): ")
    if args.week is None:
        args.week = ask("📅 Enter week number: ", int)
    if args.team is None:
        args.team = ask("🏈 Enter player's team (e.g., KC, DAL): ")
    if args.opponent_team is None:
        args.opponent_team = ask("🚩 Enter opponent team (e.g., NE, SF): ")
    # bye_week is a flag, so we leave it as-is unless you want to prompt for it too

def main():
    parser = argparse.ArgumentParser(
        description="Fantasy Football Advisor CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("--position", choices=["RB", "WR", "QB"])
    parser.add_argument("--defense_rank", type=int)
    parser.add_argument("--weather")
    parser.add_argument("--week", type=int)
    parser.add_argument("--team")
    parser.add_argument("--opponent_team")
    parser.add_argument("--bye_week", action="store_true")

    args = parser.parse_args()

    # Prompt for missing values
    prompt_if_missing(args, parser)

    print("🏈 Running Gridiron_GPT Pipeline...")

    # Semantic pipeline
    pipeline = SemanticPipeline()
    matches, index, embeddings = pipeline.run()

    print(f"FAISS index size: {index.ntotal if index else 'Index not built'}")
    print(f"First embedding: {embeddings[0][:5] if embeddings else 'No embeddings'}")

    print("🔍 Top Semantic Matches:")
    for i, match in enumerate(matches[:3]):
        print(f"  {i+1}. {match}")

    # Structured pipeline
    df, le_position, le_weather, model = load_pipeline()

    action = predict_action(
        model, le_position, le_weather,
        le_team, le_opp_team,
        args.position, args.defense_rank, args.weather,
        args.week, args.team, args.opponent_team
    )

    print(f"\n🏈 Recommended Action: {action.upper()}")

if __name__ == "__main__":
    main()
