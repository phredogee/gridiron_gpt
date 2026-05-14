# phred/cli/doctor.py

from phred.cli import register_command
from phred.semantic.audit import audit_espn, audit_nflverse
from phred.cli.utils.feedback import banner, dry_run_tip, audit_tip, warn, success, error

banner("🏈 Starting ESPN Intake")
dry_run_tip("Validating ESPN schema...")
warn("Missing player ID in row 42")
success("Ingestion complete")
error("Failed to connect to ESPN API")

@register_command("doctor", help_text="Run diagnostics")

def doctor_main():
    print("🩺 Running diagnostics...")
    doctor_cli()
    import argparse

    print("🩺 Starting semantic audit...")

    parser = argparse.ArgumentParser(description="Run semantic audits")
    parser.add_argument("target", choices=["semantic"], help="Audit target")
    parser.add_argument("--source", choices=["espn", "nflverse", "all"], default="all", help="Data source to audit")
    parser.add_argument("--dry-run", action="store_true", help="Preview audit without modifying anything")
    parser.add_argument("--player", type=str, help="Run targeted audit for a specific player")
    args = parser.parse_args()

    if args.source in ["espn", "all"]:
        print("📡 Auditing ESPN bios...")
        audit_espn(player=args.player, dry_run=args.dry_run)

    if args.source in ["nflverse", "all"]:
        print("📊 Auditing nflverse stats...")
        audit_nflverse(player=args.player, dry_run=args.dry_run)

    print("✅ Audit complete.")
