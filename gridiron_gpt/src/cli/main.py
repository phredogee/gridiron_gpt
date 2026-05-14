# src/cli/main.py

import argparse
from intake.espn_fetch import fetch_espn_data

def main():
    parser = argparse.ArgumentParser(description="Run ESPN intake and semantic merge diagnostics.")
    parser.add_argument("--dry-run", action="store_true", help="Preview ESPN fetch and merge diagnostics without committing changes.")
    args = parser.parse_args()

    print("📡 Starting ESPN intake...")
    espn_data = fetch_espn_data(dry_run=args.dry_run)

    if not args.dry_run:
        print("✅ Live fetch complete. Ready for downstream processing.")

if __name__ == "__main__":
    main()
