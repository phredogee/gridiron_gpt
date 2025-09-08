# phred/sports/fetch_registy.py

from .fetch import fetch_from_espn
from .local_fetch import fetch_local_data
from .api_fetch import fetch_api_data
from .scrape_fetch import fetch_scrape_data

def get_fetchers():
    return {
        "local": fetch_local_data,
        "api": fetch_api_data,
        "scrape": fetch_scrape_data,
        "espn": fetch_from_espn,
    }
