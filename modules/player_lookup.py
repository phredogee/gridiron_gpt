# modules/player_lookup.py

PLAYER_IDS = {
    "bijan": 4360438,
    "gibbs": 4430727,
    # Add more as needed
}

def get_player_id(name):
    return PLAYER_IDS.get(name.lower())
