# modules/embed_data.py

import json
import openai
import os
from modules.utils import banner

openai.api_key = os.getenv("OPENAI_API_KEY")

def embed_profile(profile, model="text-embedding-ada-002", dry_run=False):
    if isinstance(profile, dict):
        text = ", ".join(f"{k}={v}" for k, v in profile.items())
    else:
        text = str(profile)

    print(f"📦 Embedding input: {text}")

    if dry_run:
        print("🧪 Dry run mode — skipping API call.")
        return None

    try:
        response = openai.Embedding.create(input=text, model=model)
        vector = response["data"][0]["embedding"]
        print(f"✅ Embedding successful — vector length: {len(vector)}")
        return vector
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

vec = embed_profile(player)

if vec is not None:
    print(f"🎯 Vector preview: {vec[:5]}...")
else:
    print("⚠️ No vector returned — check API key or input format.")
