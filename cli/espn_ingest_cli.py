# /gridiron_gpt/cli/espn_ingest_cli.py

import argparse
from gridiron_gpt.semantic.espn_ingest import ingest_espn_data
from gridiron_gpt.utils.banner_utils import print_banner

def main():
    parser = argparse.ArgumentParser(description="CLI wrapper for ESPN ingest")
    parser.add_argument("--week", type=int, required=True, help="Week number to ingest")
    parser.add_argument("--dry-run", action="store_true", help="Preview cleaned data without saving")
    parser.add_argument("--banner", action="store_true", help="Enable expressive onboarding banners")
    args = parser.parse_args()

    print_banner("🚀 Launching ESPN ingest CLI", level="info")
    ingest_espn_data(week=args.week, dry_run=args.dry_run, banner=args.banner)

if __name__ == "__main__":
    main()
