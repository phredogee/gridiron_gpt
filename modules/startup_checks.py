def check_mistral_api():
    key = os.getenv("MISTRAL_API_KEY")
    if not key:
        print("⚠️ Mistral API key not found")
        return False
    print("🧠 Mistral API key detected")
    return True

def banner(provider):
    emoji = {"mistral": "🧠", "openai": "🤖"}.get(provider, "❓")
    print(f"{emoji} Using {provider.title()} for embeddings")
