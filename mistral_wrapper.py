# gridiron_gpt/mistral_wrapper.py

from importlib import import_module
from importlib.metadata import version, PackageNotFoundError

def run_mistral_diagnostics():
    try:
        v = version("mistral")
        print(f"📦 Mistral SDK version: {v}")
    except PackageNotFoundError:
        print("🚫 Mistral SDK not found")

    try:
        import_module("mistral")
        print("✅ SDK import succeeded")
    except Exception as e:
        print(f"⚠️ Import error: {e}")

    print("🎯 Mistral diagnostics complete.\n")

def embed_text(text: str) -> list:
    from mistralai import MistralClient
    client = MistralClient()
    response = client.embeddings.create(input=[text], model="mistral-embed")
    return response.data[0].embedding
