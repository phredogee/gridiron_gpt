# gridiron_gpt/semantic/intake/__init__.py

"""Intake package: fetch, clean, store, and embed player data.

This package exposes:
- get_raw_player_data: source-aware data fetching
- clean_player_data: preprocessing and normalization
- save_player_data: persistence layer
- embed_player_data: vectorization for semantic search
- FETCHERS: registry mapping source names to fetch callables
"""

from .fetch import get_raw_player_data
from .preprocess import clean_player_data
from .store import save_player_data, maybe_store_data
from .embed import embed_player_data

# Registry of available data sources for easy discovery and extension
FETCHERS = {
    "local": lambda: get_raw_player_data("local"),
    "api": lambda: get_raw_player_data("api"),
    "scrape": lambda: get_raw_player_data("scrape"),
}

def maybe_store_data(data, dry_run=False):
    if dry_run:
        print("🛑 [store] Dry-run mode — skipping file write.")
        print(f"Preview: {data[:2]} ...")
        return
    save_player_data(data)

__all__ = [
    "get_raw_player_data",
    "clean_player_data",
    "save_player_data",
    "embed_player_data",
    "FETCHERS",
]
