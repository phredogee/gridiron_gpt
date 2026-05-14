# fetchers/main.py

def fetch_player_data(source: str) -> list[dict]:
    # Your fetching logic here
    return [{"name": "Patrick Mahomes", "team": "Chiefs"}]

if __name__ == "__main__":
    data = fetch_player_data("nfl_api")
    print(data)
