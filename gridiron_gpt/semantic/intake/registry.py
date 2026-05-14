# gridiron_gpt/semantic/intake/registry.py

from phred.sports.fetch import _espn_fetcher
import datetime
def current_season():
    return datetime.datetime.now().year

FETCHERS = {
    "local":  lambda: get_raw_player_data("local"),
    "api":    lambda: get_raw_player_data("api"),
    "scrape": lambda: get_raw_player_data("scrape"),
    "espn": lambda: _espn_fetcher(season=current_season(), dry_run=True),
}

def describe_registry():
    print("📦 Semantic fetch registry:")
    for mode in FETCHERS:
        print(f"  - {mode} ✅")
