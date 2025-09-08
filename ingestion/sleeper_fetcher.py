import requests
from config.endpoints import SLEEPER_PLAYER_URL
from utils.cache import save_cache
from utils.logger import logger

def fetch_player_data():
    try:
        response = requests.get(SLEEPER_PLAYER_URL)
        response.raise_for_status()
        data = response.json()
        normalized = {
            pid: {
                "name": player.get("full_name"),
                "position": player.get("position"),
                "team": player.get("team"),
                "status": player.get("status")
            }
            for pid, player in data.items()
            if player.get("position") in ["QB", "RB", "WR", "TE"]
        }
        save_cache(normalized)
        logger.info(f"Fetched {len(normalized)} players from Sleeper.")
        return normalized
    except Exception as e:
        logger.error(f"Failed to fetch Sleeper data: {e}")
        return {}
