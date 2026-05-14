# /modules/semantic_profile.py

from modules.fetch_espn import fetch_stats
from modules.embed_data import embed_profiles
from modules.utils import banner
from modules.espn_api import fetch_player_data
from embed_client import EmbedClient
import argparse

parser = argparse.ArgumentParser(description="Build semantic player profiles")
parser.add_argument("--players", nargs="+", help="List of player names")
parser.add_argument("--metrics", nargs="+", help="List of metrics to fetch")
parser.add_argument("--dry-run", action="store_true", help="Run in dry-run mode")
args = parser.parse_args()

for player in args.players:
    stats = fetch_stats(player, args.metrics)
    if stats:
        embed_profiles(player, stats)

def build_profile_vector(profile, provider="mistral"):
    client = EmbedClient(provider=provider)
    return client.embed(profile)

def build_semantic_profiles(players, metrics=None, source="espn", dry_run=False):
    banner("🔍 Semantic Profile Builder")
    profiles = get_player_stats(players, metrics=metrics)
    embed_profiles(profiles, source=source, dry_run=dry_run)

if __name__ == "__main__":
    players = ["Bijan Robinson", "Jahmyr Gibbs"]
    metrics = ["snap_share", "red_zone_touches", "target_share"]
    build_semantic_profiles(players, metrics=metrics, dry_run=True)

