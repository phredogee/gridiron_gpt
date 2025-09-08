# gridiron_gpt/provider_banner.py

def get_banner(provider: str) -> str:
    provider = provider.lower()
    if provider == "mistral":
        return "🐉 Mistral Diagnostics\n──────────────────────"
    elif provider == "openai":
        return "🤖 OpenAI Diagnostics\n─────────────────────"
    else:
        return f"❓ Unknown Provider: {provider}\n──────────────────────────────"
