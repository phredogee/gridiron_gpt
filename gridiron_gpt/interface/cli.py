# /gridiron_gpt/interface/cli.py

print("📦 [store] Module loaded")

import argparse
from intake.fetch import get_raw_player_data
from intake.preprocess import clean_player_data
from intake.store import save_player_data
from intake.embed import embed_player_data
from interface.commands import predict, advise, ingest, schedule

def main():
    parser = argparse.ArgumentParser(description="Fantasy Football Advisor CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Register each subcommand
    predict.register(subparsers)
    advise.register(subparsers)
    ingest.register(subparsers)
    schedule.register(subparsers)

    args = parser.parse_args()
    args.func(args)

def run_intake_pipeline(dry_run=False):
    raw = get_raw_player_data()
    cleaned = clean_player_data(raw)

    save_player_data(cleaned, dry_run=dry_run)
    embed_player_data(cleaned, dry_run=dry_run)

    print("✅ Intake pipeline complete.")

if __name__ == "__main__":
    main()
