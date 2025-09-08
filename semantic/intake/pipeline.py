# intake/pipeline.py

from .fetch import fetch_player_data as get_raw_player_data
from intake.utils import clean_player_data
from intake.store import save_player_data

def run_intake():
    raw_data = fetch_player_data("nfl_api")
    processed = clean_player_data(raw_data)
    save_player_data(processed)

if __name__ == "__main__":
    run_intake()
