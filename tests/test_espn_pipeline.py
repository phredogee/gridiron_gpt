# test_espn_pipeline.py

from phred.sports.fetch import fetch_from_espn
from phred.sports.fetch import get_player_bios
from gridiron_gpt import align_embeddings

def test_pipeline(season="2025", dry_run=True):
    print(f"📅 Testing ESPN intake for season {season} | Dry-run: {dry_run}")

    data = fetch_from_espn(season=season, dry_run=dry_run)
    players = data.get("players", [])
    print(f"🏈 Fetched {len(players)} players")

    bios = get_player_bios(players, dry_run=dry_run)
    print(f"📘 Enriched {len(bios)} bios")

    merged = align_embeddings(players, bios)
    print(f"🧬 Merged {len(merged)} player profiles")

    for name, entry in merged.items():
        print(f"🔹 {name}")
        print(f"   Bio: {entry['bio']['bio']}")
        print(f"   Embedding: {entry['embedding']['embedding']}")
        print(f"   Match: {entry['position_match']}")
        print()

if __name__ == "__main__":
    test_pipeline()
