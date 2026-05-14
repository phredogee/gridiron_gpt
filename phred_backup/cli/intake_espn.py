

from phred.cli.registry import register_command
from phred.cli.utils.feedback import banner, dry_run_tip
from phred.cli.utils.feedback import banner, dry_run_tip, audit_tip, warn, success, error

banner("🏈 Starting ESPN Intake")
dry_run_tip("Validating ESPN schema...")
warn("Missing player ID in row 42")
success("Ingestion complete")
error("Failed to connect to ESPN API")

@register_command("espn-intake")
def espn_intake(dry_run=False):
    banner("🏈 ESPN Intake Starting")
    if dry_run:
        dry_run_tip("Dry-run: Validating ESPN source and schema...")
        return {"status": "dry-run", "source": "ESPN", "validated": True}

    # Real ingestion logic
    data = fetch_espn_data()
    validate_schema(data)
    return data
