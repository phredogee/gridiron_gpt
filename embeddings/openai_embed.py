# embeddings/openai_embed.py

def embed_with_openai(text: str, dry_run: bool = False):
    if dry_run:
        print(f"🤖 [OpenAI] Would embed: {text[:50]}...")
        return None

    # Real embedding logic here
    import openai
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response["data"][0]["embedding"]
