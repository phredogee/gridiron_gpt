# /gridiron_gpt/diagnostics_cli.py

import typer
from gridiron_gpt.provider_banner import get_banner
from gridiron_gpt.provider_guard import detect_installed_providers
from gridiron_gpt.mistral_wrapper import run_mistral_diagnostics
from gridiron_gpt.openai_wrapper import run_openai_diagnostics

app = typer.Typer()

@app.command()
def check(provider: str = typer.Option("auto", help="Which provider to diagnose")):
    if provider == "auto":
        provider = detect_installed_providers()[0]  # Pick first available

    print(get_banner(provider))
    print(f"🔍 Running diagnostics for provider: {provider}\n")

    if provider == "mistral":
        run_mistral_diagnostics()
    elif provider == "openai":
        run_openai_diagnostics()
    else:
        print(f"❌ Unknown provider: {provider}")
