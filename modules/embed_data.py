# modules/embed_data.py
"""
✅ Normalize input early (dict → list) to simplify logic
✅ Use clear variable names (profiles, texts, vectors)
✅ Separate dry-run logic from live API calls
✅ Return structured output for diagnostics and testing
🚫 Don’t mix batch and single logic without normalization
"""

import json
import openai
import os
from modules.utils import banner

openai.api_key = os.getenv("OPENAI_API_KEY")

def embed_profiles(profiles, model="text-embedding-ada-002", dry_run=False):
    """
    Embed one or more player profiles using OpenAI's embedding API.
    Accepts a single dict or a list of dicts.
    """
    if isinstance(profiles, dict):
        profiles = [profiles]  # Normalize to list

    texts = [", ".join(f"{k}={v}" for k, v in p.items()) for p in profiles]
    print(f"📦 Embedding input preview: {texts[:1]}...")

    if dry_run:
        print("🧪 Dry run mode — skipping API call.")
        return {
            "model": model,
            "vectors": [],
            "dry_run": True
        }

    try:
        response = openai.Embedding.create(input=texts, model=model)
        vectors = [r["embedding"] for r in response["data"]]
        print(f"✅ Embedding successful — {len(vectors)} vectors returned")
        return {
            "model": model,
            "vectors": vectors,
            "dry_run": False
        }
    except Exception as e:
        print(f"❌ Embedding failed: {e}")
        return None

# --- Test Case ---
player = {
    "name": "Bijan Robinson",
    "snap_share": 0.68,
    "red_zone_touches": 12,
    "team": "Falcons"
}

vec = embed_profiles(player)

if vec is not None:
    print(f"🎯 Vector preview: {vec[:5]}...")
else:
    print("⚠️ No vector returned — check API key or input format.")
