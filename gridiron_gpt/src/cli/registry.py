# src/cli/registry.py

import typer
from dashboard.tag_roles import tag_roles, ROLE_TAGS
from dashboard.prepare_dashboard import prepare_dashboard
from intake.load_players import load_players  # or wherever your bios come from

@cli.command()
def preview_tagged_dashboard(
    min_confidence: float = 0.6,
    sort_by: str = "role_tag"
):
    players = load_players()
    tagged = tag_roles(players, ROLE_TAGS)
    prepare_dashboard(tagged, min_confidence=min_confidence, sort_by=sort_by, dry_run=True)

