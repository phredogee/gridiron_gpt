# gridiron_gpt/cli/espn.py

import click
from gridiron_gpt.semantic.espn_ingest import ingest_espn_data, dry_run_intake
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
    """📥 Ingest ESPN player data"""
    if dry_run:
        dry_run_intake(week=week, banner=banner)
    else:
        ingest_espn_data(week=week, dry_run=False, banner=banner)

@espn.command()
def dry_run():
    """🔍 Preview ESPN player intake and validate structure"""
    dry_run_intake()

@espn.command()
def fix():
    """🛠️ Patch missing ESPN player entries"""
    patch_missing_players()
