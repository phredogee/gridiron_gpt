# / gridiron_gpt/phred/cli/semantic_cli.py

import argparse
from semantic.profile_data import load_cleaned_data
from semantic.profile_delta import compute_profile_delta
from semantic.matchup_diff import compute_matchup_diff
from semantic.roster_embed import embed_roster
from semantic.utils.feedback import banner

def main():
    parser = argparse.ArgumentParser(description="Run semantic modules directly")
    parser.add_argument("--source", choices=["espn", "nflverse"], required=True)
    parser.add_argument("--identifier", required=True, help="Week or season")
    parser.add_argument("--profile", required=True)
    parser.add_argument("--delta", action="store_true")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--embed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = load_cleaned_data(args.source, args.identifier, args.profile)

    if args.dry_run:
        banner("🧪 Dry Run")
        print(f"Loaded {len(data)} records from {args.source}/{args.profile}_{args.identifier}")
        return

    if args.delta:
        banner("📈 Profile Delta")
        pprint(compute_profile_delta(data))

    if args.diff:
        banner("⚔️ Matchup Diff")
        team_a, team_b = split_matchup(data)
        pprint(compute_matchup_diff(team_a, team_b))

    if args.embed:
        banner("🧬 Roster Embeddings")
        pprint(embed_roster(data["roster"]))

if __name__ == "__main__":
    main()
