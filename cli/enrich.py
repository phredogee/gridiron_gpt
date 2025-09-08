# cli/enrich.py

import click
from semantic.espn_ingest import fetch_espn_players

@click.command()
def espn():
    """Ingest and display ESPN player data."""
    players = fetch_espn_players()
    if not players:
        click.echo("🚫 No data retrieved.")
        return
    click.echo(f"📊 ESPN Players Loaded: {len(players)}")
