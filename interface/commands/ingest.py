# interface/commands/ingest.py

from interface.cli import run_intake_pipeline

def register(subparsers):
    parser = subparsers.add_parser("ingest", help="Ingest or rebuild data")
    parser = argparse.ArgumentParser(
        description="Fantasy Football Advisor CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
    # Existing flags
    parser.add_argument("--rebuild", action="store_true", help="Force rebuild of data")
    parser.add_argument("--ingest", action="store_true", help="Run ingestion pipeline")

    # New flag for testing
    parser.add_argument("--dry-run", action="store_true", help="Skip saving and embedding")

    parser.set_defaults(func=run_ingest)

def run_ingest(args):
    print("📦 [ingest] Starting intake pipeline...")
    print(f"🔧 Flags: rebuild={args.rebuild}, ingest={args.ingest}, dry_run={args.dry_run}")

    if args.rebuild:
        print("🧹 [rebuild] Rebuilding data from scratch...")
        # TODO: Add rebuild logic here

    if args.ingest:
        print("🍽️ [ingest] Running ingestion pipeline...")
        run_intake_pipeline(dry_run=args.dry_run)

    if not args.rebuild and not args.ingest:
        print("⚠️ No action specified. Use --rebuild and/or --ingest.")
