# fetchers/__main__.py

from .main import fetch_player_data

if __name__ == "__main__":
    data = fetch_player_data("nfl_api")
    print(data)
