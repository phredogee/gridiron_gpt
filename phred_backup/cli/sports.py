# phred/cli/sports.py

from phred.cli.registry import register_command
from phred.sports.fetchers.stats import fetch_player_stats as fetch_raw_stats
from phred.sports.merge import (
    fetch_player_stats,
    fetch_pbp_data,
    merge_stats,
    save_merged_stats,
    fetch_espn_bios
)

print("🧠 CLI wrapper loaded")

def fetch_pbp_data() -> list:
    """Stub for fetching play-by-play data."""
    print("📡 Fetching PBP data...")
    return []

def merge_stats(player_data: dict, pbp_data: dict) -> list:
    """Stub for merging player bios and PBP events."""
    print("🧠 Merging stats...")
    return player_data.get("players", [])

def save_merged_stats(merged: list) -> None:
    """Stub for saving merged stats."""
    print(f"💾 Saving {len(merged)} merged players...")

@register_command("merge")
def run_merge(dry_run=False, backend="openai"):
    player_data = {"players": fetch_espn_bios(backend=backend)}
    pbp_data = {"events": []}  # Optional for now

    merged = merge_stats(player_data, pbp_data)

    if dry_run:
        print("\n🧠 Semantic Merge Preview\n" + "─" * 30)
        for player in merged:
            name = player.get("fullName")
            bio = player.get("bio", "")
            embedding = player.get("embedding")
            if not embedding:
                print(f"⚠️ {name}\n   Missing bio or embedding. Skipped.\n")
            else:
                richness = embedding["vector"][0]
                print(f"✅ {name} — Richness: {richness}\n   \"{embedding['summary']}\"\n")
        return

    print(f"✅ Merged {len(merged)} players.")

@register_command("fetch")
def run_fetch(dry_run=False):
    print("📡 Running fetch stub...")
    if dry_run:
        print("🧪 Dry-run: fetch logic not executed.")

@register_command("save")
def run_save(dry_run=False):
    print("💾 Running save stub...")
    if dry_run:
        print("🧪 Dry-run: save logic not executed.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview semantic merge without saving")
    parser.add_argument("--backend", choices=["openai", "mistral"], default="openai",
                        help="Embedding backend to use")
    args = parser.parse_args()

    run_merge(dry_run=args.dry_run, backend=args.backend)
