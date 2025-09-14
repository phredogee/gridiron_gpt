# test_espn_pipeline.py

# 🧪 Onboarding Tip:
# ✅ Use named arguments for clarity in test calls
# ✅ Avoid redundant calls to the same function
# ✅ Always reference the correct variable—`result`, not `data`

from phred.sports.espn import fetch_from_espn
from phred.sports.espn import get_player_bios
from gridiron_gpt import align_embeddings

def test_pipeline():
    season = 2025
    dry_run = True
    result = fetch_from_espn(season=season, dry_run=dry_run)

    players = result.get("players", [])
    print(f"🏈 Fetched {len(players)} players")

    bios = get_player_bios(players, dry_run=dry_run)
    print(f"📘 Enriched {len(bios)} bios")

    if not players or not bios:
        print("⚠️ Skipping merge due to missing data")
        return

    merged = align_embeddings(players, bios)
    print(f"🧬 Merged {len(merged)} player profiles")

    for name, entry in merged.items():
        print(f"🔹 {name}")
        print(f"   Bio: {entry['bio']['bio']}")
        print(f"   Embedding: {entry['embedding']['embedding']}")
        print(f"   Match: {entry['position_match']}")
        print()
