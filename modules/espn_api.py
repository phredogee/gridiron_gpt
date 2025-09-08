# modules/espn_api.py

import requests

BASE_URL = "https://site.api.espn.com/apis/fantasy/v2/games/ffl"

def fetch_player_data(player_name):
    # Placeholder logic — you’ll want to map names to ESPN IDs
    url = f"{BASE_URL}/players?search={player_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Failed to fetch data for {player_name}")
        return None
