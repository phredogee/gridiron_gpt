# /mistral_embed/cli.py

import typer
from mistral_embed.embed import embed_text
from mistral_embed.utils import banner, warn

app = typer.Typer()

@app.command()
def embed(
    text: str = typer.Option(None, help="Text to embed"),
    file: str = typer.Option(None, help="Path to file with text"),
    dry_run: bool = typer.Option(False, help="Preview input without embedding"),
    verbose: bool = typer.Option(False, help="Show diagnostics"),
):
    banner("🔍 Mistral Embedding CLI")

    if not text and not file:
        warn("❌ Provide either --text or --file")
        raise typer.Exit()

    input_text = text or open(file).read()

    if dry_run:
        print("🧪 Dry run: input preview")
        print(input_text)
        raise typer.Exit()

    if verbose:
        print(f"📏 Input length: {len(input_text)} characters")

    embedding = embed_text(input_text)
    print("✅ Embedding successful")
    print(embedding)
