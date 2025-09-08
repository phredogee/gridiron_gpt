# /semantic_pipeline/embed_cli.py
"""
🧠 Mistral Embedding CLI
Generates embeddings for input text using Mistral SDK.
"""

import os
import typer
from mistralai import Mistral
from rich import print
from semantic.utils.feedback import banner

app = typer.Typer()

def check_env_key():
    key = os.environ.get("MISTRAL_API_KEY")
    if not key:
        banner("❌ Missing MISTRAL_API_KEY", style="error")
        raise SystemExit("🔒 Cannot proceed without API key.")
    banner("🔑 API key loaded", style="success")
    return key

@app.command()
def embed(
    text: str = typer.Argument(..., help="Text to embed"),
    model: str = typer.Option("mistral-embed", help="Embedding model name"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print config without calling API"),
):
    banner("🔍 Mistral Embedding CLI")

    api_key = check_env_key()

    if dry_run:
        print(f"🚫 Dry run mode enabled. Would embed:\n[italic]{text}[/italic]\nUsing model: [green]{model}[/green]")
        return

    try:
        client = Mistral(api_key=api_key)
        response = client.embeddings.create(model=model, inputs=[text])
        banner("✅ Embedding response")
        print(response.data)
    except Exception as e:
        banner("❌ Error during embedding", style="error")
        print(f"[red]{e}[/red]")

if __name__ == "__main__":
    app()
