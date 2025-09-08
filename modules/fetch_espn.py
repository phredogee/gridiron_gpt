# modules/fetch_espn.py

from modules.player_lookup import get_player_id
import requests

def fetch_stats(player_name, metrics):
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
