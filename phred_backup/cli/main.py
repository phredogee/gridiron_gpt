# phred/cli/main.py

import argparse
import warnings

from phred.cli.sports import run_fetch, run_merge, run_save
from phred.sports.fetch import fetch_player_data
from phred.sports.fetchers.espn.bios import get_player_bios
# near the top of phred/cli/main.py
from phred.sports.fetchers.espn.diagnostics import (
    diagnose_espn_fetch,
    diagnose_semantic_index,
    diagnose_shell_env
)

warnings.filterwarnings("ignore", category=RuntimeWarning)

def main():
    parser = argparse.ArgumentParser(description="Run the sports pipeline")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--season", type=str, default="2024", help="NFL season to fetch")
    parser.add_argument("--dry-run", action="store_true", help="Preview semantic merge without saving")
    parser.add_argument("--source", type=str, default="espn", help="Data source (espn, nfl_api)")
    parser.add_argument("--limit", type=int, default=5, help="Limit dashboard preview rows")
    parser.add_argument("--steps", nargs="+", choices=["fetch", "merge", "save"], default=["fetch", "merge", "save"],
                        help="Pipeline steps to execute")
    parser.add_argument("--outdir", type=str, default="data", help="Output directory for saved files")
    parser.add_argument("--list-steps", action="store_true", help="List available pipeline steps")

    args = parser.parse_args()
    print("🚀 Running sports pipeline...")
    print(f"📅 Season: {args.season} | Source: {args.source}")
    print(f"🧪 Dry-run mode: {'ON' if args.dry_run else 'OFF'}")
    print(f"📦 Steps: {', '.join(args.steps)}")

    try:
        data = fetch_player_data(season=int(args.season), source=args.source)
        players = data.get("players", [])
        bios = get_player_bios(players, dry_run=args.dry_run) if players else []
    except Exception as e:
        print(f"❌ Failed to fetch or enrich data: {e}")
        data = {}
        bios = {}

    if args.verbose:
        print("🏈 Starting sports pipeline...")
        print(f"📅 Season: {args.season} | Source: {args.source}")
        print(f"🧪 Dry-run mode: {'ON' if args.dry_run else 'OFF'}")
        print(f"📦 Steps: {', '.join(args.steps)}")


    if args.doctor:
        diagnose_espn_fetch(season=args.season, dry_run=args.dry_run)
        diagnose_semantic_index()
        diagnose_shell_env()

    if "fetch" in args.steps:
        run_fetch(season=args.season, source=args.source, dry_run=args.dry_run)

    if "merge" in args.steps:
        run_merge(season=args.season, source=args.source, dry_run=args.dry_run, bios=bios)

    if "save" in args.steps:
        run_save(outdir=args.outdir, season=args.season, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

with open("pipeline.log", "a") as log:
    log.write(f"[{args.season}] {args.steps} run at {datetime.now().isoformat()}\n")
