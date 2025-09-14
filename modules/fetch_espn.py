# modules/fetch_espn.py
# Avoid self-imports—define and call functions locally unless modular reuse is needed.

from modules.player_lookup import get_player_id
import requests

def fetch_stats(player, metrics=None):
    # Stubbed for CLI feedback testing
    return {
        "name": player,
        "metrics": metrics or [],
        "stats": {"snap_share": 0.65, "target_share": 0.22}
    }

def get_player_stats(player_name, metrics):
    player_id = get_player_id(player_name)
    if not player_id:
        print(f"❌ Unknown player: {player_name}")
        return None

    url = f"https://site.api.espn.com/apis/fantasy/v2/games/ffl/players/{player_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Failed to fetch data for {player_name}")
        return None

    data = response.json()
    normalized = {metric: data.get("stats", {}).get(metric, "N/A") for metric in metrics}
    return normalized
