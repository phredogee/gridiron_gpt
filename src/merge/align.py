# gridiron_gpt/src/merge/align.py

def align_embeddings(players: list, bios: dict) -> dict:
    aligned = {}

    for player in players:
        name = player.get("name")
        position = player.get("position", "Unknown")
        bio = bios.get(name)

        if not bio:
            print(f"⚠️ No bio found for {name}")
            continue

        # Stubbed embedding logic (replace with real vector lookup later)
        embedding = {
            "embedding": [0.1, 0.2, 0.3],
            "position": position
        }

        aligned[name] = {
            "bio": bio,
            "embedding": embedding,
            "position_match": bio["position"] == position
        }

        print(f"✅ Aligned {name} | Position match: {bio['position']} vs {position}")

    return aligned
