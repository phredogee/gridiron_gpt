# phred/sports/merge.py

from datetime import datetime
from phred.sports.pipeline.semantic import run_semantic_pipeline
from phred.sports.embed import embed_bio
from phred.cli.utils import feedback  # emoji banners, dry-run output

# 🧠 Semantic merge pipeline
def run_merge(players: list[dict], dry_run: bool = True) -> list[dict]:
    embeddings = run_semantic_pipeline(players, dry_run=dry_run)

    for player in players:
        name = player.get("name")
        matching = next((e for e in embeddings if e.get("name") == name), None)

        if matching:
            player.update({
                "embedding": matching["embedding"],
                "bio": matching.get("bio"),
                "position": matching.get("position")
            })

            if dry_run:
                print(feedback.banner(f"🧬 {name}", "info"))
                print(f"   📘 Bio: {player['bio']}")
                print(f"   🧠 Embedding: {player['embedding'][:5]}...")
                print(f"   🧩 Position: {player['position']}\n")

    if not dry_run:
        print(feedback.success("Merge complete. Ready for downstream save or dashboard."))

    return players

# 🔀 Merge event streams from multiple sources
def merge_events(events: list, nflverse: list) -> list:
    print(feedback.banner("🔀 Merging event streams...", "info"))

    def normalize(e):
        return {
            "playerId": e.get("playerId"),
            "type": e.get("type"),
            "team": e.get("team"),
            "date": datetime.strptime(e.get("date"), "%Y-%m-%d").date(),
            "source": e.get("source", "unknown")
        }

    combined = [normalize(e) | {"source": "nfl_api"} for e in events] + \
               [normalize(e) | {"source": "nflverse"} for e in nflverse]

    seen = set()
    deduped = []
    for e in combined:
        key = (e["playerId"], e["type"], e["date"])
        if key not in seen:
            seen.add(key)
            deduped.append(e)

    print(feedback.success(f"✅ Merged {len(deduped)} unique events"))
    return deduped

# 🧪 Stubbed functions for CLI import compatibility
def merge_stats(*args, **kwargs):
    print(feedback.banner("Stubbed merge_stats — implement real logic", "warning"))
    return {"merged": "placeholder"}

def fetch_pbp_data(*args, **kwargs):
    print(feedback.banner("Stubbed fetch_pbp_data — implement real logic", "warning"))
    return {"pbp": "placeholder"}

# 🧪 CLI entry point
if __name__ == "__main__":
    import argparse
    from phred.sports.fetchers.espn.players import get_players

    parser = argparse.ArgumentParser(description="Run semantic merge pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Preview merged output without saving")
    args = parser.parse_args()

    players = get_players()
    merged = run_merge(players, dry_run=args.dry_run)

    if args.dry_run:
        print(feedback.banner("🧪 Dry-run complete. No data saved.", "info"))
    else:
        print(feedback.banner("💾 Ready to save or pass to dashboard prep.", "success"))

# Deduplicate by (playerId, type, date)
def deduplicate_events(events: list) -> list:
    seen = set()
    merged = []
    for e in events:
        key = (e["playerId"], e["type"], e["date"])
        if key not in seen:
            seen.add(key)
            merged.append(e)
    print(feedback.success(f"✅ Merged {len(events)} → {len(merged)} unique events"))
    return merged

def merge_events(events: list, nflverse: list) -> list:
    print(feedback.banner("🔀 Merging event streams...", "info"))

    def normalize(e):
        return {
            "playerId": e.get("playerId"),
            "type": e.get("type"),
            "team": e.get("team"),
            "date": datetime.strptime(e.get("date"), "%Y-%m-%d").date(),
            "source": e.get("source", "unknown")
        }

    combined = [normalize(e) | {"source": "nfl_api"} for e in events] + \
               [normalize(e) | {"source": "nflverse"} for e in nflverse]

    return deduplicate_events(combined)

# 🧬 ESPN bio enrichment
def fetch_espn_bios(backend="openai") -> list[dict]:
    raw_bios = [...]  # TODO: Replace with actual ESPN intake
    enriched = []
    for player in raw_bios:
        embedding = embed_bio(player["bio"], backend=backend)
        player["embedding"] = embedding
        enriched.append(player)
    return enriched

# 📊 Player stats stub
def fetch_player_stats(player_id: str, source: str = "espn") -> dict:
    print(feedback.banner(f"📊 Fetching stats for {player_id} from {source}", "info"))
    return {
        "playerId": player_id,
        "gamesPlayed": 0,
        "touchdowns": 0,
        "source": source
    }

# 🧪 Play-by-play stub
def fetch_pbp_data(*args, **kwargs):
    print(feedback.banner("Stubbed fetch_pbp_data — implement real logic", "warning"))
    return {"pbp": "placeholder"}

# 🧠 Bio embedding stub
def embed_bio(bio: str) -> dict:
    if not bio:
        return None
    return {
        "vector": [len(bio.split())],
        "summary": bio
    }
