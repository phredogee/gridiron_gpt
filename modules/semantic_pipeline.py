# gridiron_gpt/modules/semantic_profile.py

"""
✅ Match function names and signatures across modules
✅ Use dry-run mode to isolate embedding logic
✅ Pass metadata like source for diagnostics and logging
✅ Keep semantic pipelines modular and banner-rich
🚫 Don’t assume early scaffolding matches current expectations
"""

from modules.embed_data import embed_profiles
from modules.fetch_espn import get_player_stats
from modules.utils import banner, log_dry_run
from modules.semantic_profile import build_semantic_profiles, build_profile_vector


class SemanticPipeline:
    def __init__(self, source="espn", dry_run=False, provider="mistral"):
        self.source = source
        self.dry_run = dry_run
        self.provider = provider

    def build_profiles(self, players, metrics=None):
        banner("🔍 SemanticPipeline: Building profiles")
        build_semantic_profiles(players, metrics=metrics, source=self.source, dry_run=self.dry_run)

    def embed_single_profile(self, profile):
        banner("📦 Embedding single profile")
        return build_profile_vector(profile, provider=self.provider)

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

def embed_profiles(profiles, source=None, model="text-embedding-ada-002", dry_run=False):
    if dry_run:
        return {
            "model": model,
            "vectors": [],
            "dry_run": True
        }
