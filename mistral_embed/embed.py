import requests
import os

MISTRAL_API_URL = "https://api.mistral.ai/v1/embeddings"
API_KEY = os.getenv("MISTRAL_API_KEY")

def embed_text(text: str) -> list:
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"input": text, "model": "mistral-embed"}
    response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]
