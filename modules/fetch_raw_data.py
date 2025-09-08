# modules/fetch_raw_data.py

import requests
from modules.utils import load_config

config = load_config()

def get_fantasypros_rankings(position="QB", week=1):
    """Fetch weekly rankings from FantasyPros."""
    base_url = config["fantasypros"]["base_url"]
    api_key = config["fantasypros"]["api_key"]
    
    endpoint = f"{base_url}/rankings/{position}?week={week}&apikey={api_key}"
    response = requests.get(endpoint)
    
    if response.status_code != 200:
        raise Exception(f"FantasyPros API error: {response.status_code}")
    
    return response.json()

def get_sleeper_player_updates():
    """Fetch player updates from Sleeper."""
    base_url = config["sleeper"]["base_url"]
    endpoint = f"{base_url}/players/nfl"
    
    response = requests.get(endpoint)
    
    if response.status_code != 200:
        raise Exception(f"Sleeper API error: {response.status_code}")
    
    return response.json()

# modules/fetch_raw_data.py

def fetch_player_data(player_name: str, week: int = 1):
    """Stub for fetching player data — can be expanded with real sources."""
    print(f"📊 Fetching data for {player_name}, week {week}")
    # You could call fantasypros or sleeper functions here
    return {
        "name": player_name,
        "week": week,
        "rushing_yards": 88,
        "receiving_yards": 34,
        "touchdowns": 1
    }
