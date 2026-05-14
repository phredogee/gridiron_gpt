import os
import json
from datetime import datetime

def save_nfl_events(events: list, path: str = "data/nfl_game_events.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(events, f, indent=2)

def save_merged_stats(data: dict, path: str = "data/merged_stats.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def save_json(data: dict | list, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def save_timestamped(data: dict | list, prefix: str = "data/nfl_events"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{prefix}_{timestamp}.json"
    save_json(data, path)
    print(f"🕒 Saved timestamped data to {path}")

