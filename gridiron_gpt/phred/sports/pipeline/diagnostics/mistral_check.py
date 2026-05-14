# /semantic_pipeline/diagnostics/mistral_check.py

"""
🔍 Mistral SDK Diagnostic Script
Checks import health and basic client instantiation.
"""

def banner(msg: str):
    print(f"\n🧪 {msg}\n" + "-" * 40)

def main():
    banner("Starting Mistral SDK check...")

    try:
        from mistralai.client import MistralClient
        print("✅ Import succeeded: MistralClient is available.")
    except ImportError as e:
        print(f"❌ ImportError: {e}")
        return

    try:
        client = MistralClient(api_key="sk-fake-key")
        print("✅ Client instantiated (with dummy key).")
    except Exception as e:
        print(f"⚠️ Client instantiation failed: {e}")

if __name__ == "__main__":
    main()
