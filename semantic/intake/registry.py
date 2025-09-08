# gridiron_gpt/semantic/intake/registry.py

from .fetch import get_raw_player_data, fetch_from_espn

FETCHERS = {
    "local":  lambda: get_raw_player_data("local"),
    "api":    lambda: get_raw_player_data("api"),
    "scrape": lambda: get_raw_player_data("scrape"),
    "espn":   fetch_from_espn,
}
