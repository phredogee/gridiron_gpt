import requests
from phred.sports.fetchers.fetch_players import get_players
from semantic_pipeline.embed_cli import embed

# Fetch players
players = get_players("nfl", api_key="your_fantasypros_key")
print(players.keys())  # Debug: check structure

# Build bios
bios = {
    p["player_id"]: f"{p['first_name']} {p['last_name']} is a {p['position']} for {p['team']}."
    for p in players["players"]
}

# Embed bios
for pid, bio in bios.items():
    print(f"\n📌 Embedding for: {pid}")
    embed(text=bio)
