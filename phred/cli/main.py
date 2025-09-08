# gridiron_gpt/main.py

import argparse
import spacy
from modules.semantic_pipeline import SemanticPipeline
from modules.pipeline import load_pipeline
from modules.predictor import predict_action

def run_semantic_mode(args):
    print("🧠 Semantic mode activated")
    if args.verbose:
        print("📣 Verbose mode: diagnostics and banners enabled")
    nlp = spacy.load("en_core_web_sm")
    pipeline = SemanticPipeline(nlp)
    pipeline.run(args.semantic, dry_run=args.dry_run)

def run_structured_mode(args):
    print("⚙️ Structured mode activated")
    if args.verbose:
        print("📣 Verbose mode: diagnostics and banners enabled")
    pipeline = load_pipeline()
    result = predict_action(pipeline, args)
    print(f"📈 Prediction: {result}")

def main():
    parser = argparse.ArgumentParser(
        description="🏈 GridironGPT CLI — Fantasy Football Advisor",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # 🧠 Semantic Mode
    semantic_group = parser.add_argument_group("🧠 Semantic Mode")
    semantic_group.add_argument("--semantic", type=str,
                                help="Natural language query (e.g., 'Show me rushing yards for McCaffrey')")
    semantic_group.add_argument("--verbose", action="store_true",
                                help="Enable verbose output (banners, diagnostics)")

    # 🛠️ Structured Mode
    structured_group = parser.add_argument_group("🛠️ Structured Mode")
    structured_group.add_argument("--position", choices=["RB", "WR", "QB"],
                                  help="Player position")
    structured_group.add_argument("--defense_rank", type=int,
                                  help="Opponent defense rank (1–32)")
    structured_group.add_argument("--weather",
                                  help="Weather condition (e.g., clear, rainy)")
    structured_group.add_argument("--week", type=int,
                                  help="Week number")
    structured_group.add_argument("--team",
                                  help="Player's team (e.g., KC, DAL)")
    structured_group.add_argument("--opponent_team",
                                  help="Opponent team (e.g., NE, SF)")
    structured_group.add_argument("--bye_week", action="store_true",
                                  help="Flag if player's team is on a bye week")
    structured_group.add_argument("--dry_run", action="store_true",
                                  help="Diagnostic mode")

    args = parser.parse_args()

    print("🚀 Launching GridironGPT...")

    if args.dry_run:
        print("🔍 Dry-run mode enabled — showing parsed input:")
        for arg in vars(args):
            print(f"   • {arg}: {getattr(args, arg)}")
        return

    if args.semantic:
        run_semantic_mode(args)
    else:
        run_structured_mode(args)

if __name__ == "__main__":
    main()
