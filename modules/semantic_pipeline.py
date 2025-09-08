# semantic_profile.py

from modules.embed_data import embed_profiles
from modules.fetch_espn import get_player_stats
from modules.utils import banner, log_dry_run

def build_semantic_profiles(players, metrics=None, source="espn", dry_run=False):
    banner("🔍 Semantic Profile Builder")

    # Step 1: Fetch ESPN data
    stats = get_player_stats(players, metrics=metrics)
    if dry_run:
        banner(f"🧪 Dry-run: would embed {len(players)} player profiles from {source}")
        for name in players:
            print(f"👤 {name}")
        log_dry_run(players, source=source, metrics=metrics)
        return

    # Step 2: Embed profiles
    embed_profiles(stats, source=source)

    banner("✅ Semantic embedding complete")

if __name__ == "__main__":
    # Example usage
    players = ["Bijan Robinson", "Jahmyr Gibbs"]
    metrics = ["snap_share", "red_zone_touches", "target_share"]
    build_semantic_profiles(players, metrics=metrics, dry_run=True)
