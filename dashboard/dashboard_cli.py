# gridiron_gpt/dashboard/dashboard_cli.py

import argparse
from semantic_ingestor.import_audit import audit_imports
from utils.banner_utils import banner, success_banner, warn_banner, fail_banner
from semantic.router import route_semantic_ingestion
from dashboard.matchup_summary import generate_summary
from dashboard.matchup_diff import run_matchup_diff

def main():
    banner("🧠 Semantic Dashboard CLI")

    parser = argparse.ArgumentParser(
        description="🧪 Semantic routing and dashboard diagnostics",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--dry-run", action="store_true", help="Run import audit without ingestion")
    parser.add_argument("--source", choices=["espn", "nflverse"], required=True, help="Data source")
    parser.add_argument("--week", type=int, help="Week number for ESPN")
    parser.add_argument("--season", type=int, help="Season year for nflverse")
    parser.add_argument("--team-a", type=str, help="Team A identifier")
    parser.add_argument("--team-b", type=str, help="Team B identifier")
    parser.add_argument("--summary", action="store_true", help="Generate matchup summary")
    parser.add_argument("--profile", type=str, default="default", help="Semantic profile name")
    args = parser.parse_args()

    if args.dry_run:
        print("🧪 Dry-run mode: auditing imports only...\n")
        audit_imports()
        return

    print("🚀 Starting semantic ingestion...\n")

    identifier = args.week if args.source == "espn" else args.season
    if not identifier:
        fail_banner("Missing identifier: use --week for ESPN or --season for nflverse")
        return

    if args.team_a and args.team_b and args.summary:
        summary = generate_summary(
            team_a=args.team_a,
            team_b=args.team_b,
            source=args.source,
            identifier=identifier,
            profile=args.profile
        )
        print(summary)
        return

    if args.team_a and args.team_b:
        diff = run_matchup_diff(
            team_a=args.team_a,
            team_b=args.team_b,
            source=args.source,
            identifier=identifier,
            profile=args.profile
        )
        if diff:
            print(diff)
        return

    try:
        route_semantic_ingestion(
            source=args.source,
            identifier=identifier,
            profile=args.profile,
            dry_run=args.dry_run
        )
        if args.dry_run:
            warn_banner("Dry-run mode: no data saved or persisted")
        else:
            success_banner("Semantic ingestion completed successfully")
    except Exception as e:
        fail_banner(f"Routing failed: {str(e)}")

if __name__ == "__main__":
    main()
