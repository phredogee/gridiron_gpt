import json
import os

def save_cache(data, filename="sleeper_cache.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_cache(filename="sleeper_cache.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}
