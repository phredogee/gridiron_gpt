

import typer
from mistral_wrapper import embed_text
from semantic.utils.feedback import banner

app = typer.Typer()

@app.command()
def embed(text: str, dry_run: bool = False):
    print_banner("📦 Embed CLI")
    if dry_run:
        typer.echo(f"🧪 Dry run: would embed → '{text}'")
        return
    vector = embed_text(text)
    typer.echo(f"🔢 Embedding: {vector}")
