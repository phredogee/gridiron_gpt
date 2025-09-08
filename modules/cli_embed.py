# /modules/cli_embed.py

import typer
import json
from pathlib import Path
from embed_client import EmbedClient

app = typer.Typer()

def embed_profile(profile, provider="mistral"):
    client = EmbedClient(provider=provider)
    return client.embed(profile)

@app.command()
def main(file: Path = typer.Argument(..., help="Path to JSON profile"),
         provider: str = typer.Option("mistral", help="Embedding provider")):
    """Embed a player profile from a JSON file."""
    if not file.exists():
        typer.echo(f"❌ File not found: {file}")
        raise typer.Exit(code=1)

    profile = json.loads(file.read_text())
    vec = embed_profile(profile, provider=provider)
    typer.echo(f"✅ Embedded with {provider}: {len(vec)} dimensions")
    typer.echo(f"🎯 Preview: {vec[:5]}...")

if __name__ == "__main__":
    app()
