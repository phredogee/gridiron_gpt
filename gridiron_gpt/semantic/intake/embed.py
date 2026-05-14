# gridiron_gpt/intake/embed.py

def embed_player_data(data, dry_run=False):
    print(f"🧠 [embed] Called with {len(data)} records")

    if dry_run:
        print("🛑 [embed] Dry-run mode — skipping embedding.")
        return

    # Actual embedding logic
    # e.g., vectorize, store in index
    print("✅ [embed] Embedding complete.")
