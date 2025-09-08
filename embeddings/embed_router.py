# embeddings/embed_router.py

from gridiron_gpt.embeddings.mistral_embed import embed_with_mistral
from gridiron_gpt.embeddings.openai_embed import embed_with_openai
from gridiron_gpt.provider_guard import detect_installed_providers
from gridiron_gpt.embeddings.embed_router import embed

def embed(text: str, provider: str = "auto", dry_run: bool = False):
    if provider == "auto":
        provider = detect_installed_providers()[0]

    print(f"📦 Embedding with provider: {provider}")
    if dry_run:
        print(f"🧪 Dry-run mode: no actual API calls\n")

    if provider == "mistral":
        return embed_with_mistral(text, dry_run=dry_run)
    elif provider == "openai":
        return embed_with_openai(text, dry_run=dry_run)
    else:
        raise ValueError(f"❌ Unknown provider: {provider}")
