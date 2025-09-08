
from phred.sports.doctor.espn import diagnose_espn
from phred.sports.doctor.semantic import diagnose_semantic
from phred.sports.doctor.imports import check_import_hygiene

def run_all_diagnostics(season: int = 2024, dry_run: bool = True):
    print("🩺 Running full diagnostic suite...\n")
    print("📊 ESPN diagnostics:")
    diagnose_espn(season, dry_run)
    print("\n🧠 Semantic diagnostics:")
    diagnose_semantic()
    print("\n📦 Import hygiene check:")
    check_import_hygiene()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run all diagnostics")
    parser.add_argument("--season", type=int, default=2024)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run_all_diagnostics(season=args.season, dry_run=args.dry_run)
