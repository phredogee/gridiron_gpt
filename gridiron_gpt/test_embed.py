# gridiron_gpt/test_embed.py

def test_embed_dry_run():
    from gridiron_gpt.embeddings.embed_router import embed
    text = "Bijan Robinson had 1,200 scrimmage yards as a rookie."
    result = embed(text, provider="auto", dry_run=True)
    assert result is not None  # or assert expected structure

print("🧪 Testing dry-run embedding for Bijan Robinson...")
