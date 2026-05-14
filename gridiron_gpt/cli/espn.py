# gridiron_gpt/cli/espn.py

import click
from gridiron_gpt.semantic.espn_ingest import ingest_espn_data, dry_run_intake
from gridiron_gpt.data_ingest.espn_ingest import fetch_espn_data, clean_espn_data
from gridiron_gpt.validators.profile_validator import validate_profile_schema, REQUIRED_FIELDS
from gridiron_gpt.feedback import banner

@click.group()
def espn():
    """🏈 ESPN data intake commands"""
    banner("📦 ESPN CLI module loaded.")

@espn.command()
@click.option("--week", required=True, type=int)
@click.option("--dry-run", is_flag=True)
@click.option("--banner", is_flag=True)
def intake(week, dry_run, banner):
    """📥 Ingest ESPN player data and build query index"""
    if dry_run:
        dry_run_intake(week=week, banner=banner)
        return

    players = ingest_espn_data(week=week, dry_run=False, banner=banner)

    if players:
        from gridiron_gpt.core.advisor import Advisor
        advisor = Advisor()
        advisor.build_from_players(players)
        advisor.save()

@espn.command()
@click.option("--week", required=True, type=int, help="NFL week number to preview")
def dry_run(week):
    """🔍 Preview ESPN player intake and validate structure"""
    dry_run_intake(week=week, banner=True)

@espn.command()
@click.option("--week", required=True, type=int, help="NFL week number to scan for missing entries")
def fix(week):
    """🛠️ Patch missing ESPN player entries"""
    banner("🔍 Scanning for missing player entries...")
    data = fetch_espn_data(week)
    cleaned = clean_espn_data(data)
    missing = [
        entry for entry in cleaned
        if any(field not in entry or entry[field] is None for field in REQUIRED_FIELDS)
    ]
    if missing:
        banner(f"⚠️ Found {len(missing)} incomplete entries:")
        for entry in missing:
            print(f"  - {entry.get('profile_id', 'unknown')}: {entry}")
    else:
        banner("✅ No missing entries found.")
