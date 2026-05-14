# phred/sports/__init__.py

"""
Sports data pipeline for player stats, predictions, and CLI integration.
"""

# 🧩 Core fetchers
from .fetchers.espn import fetch_from_espn
from .fetchers.nfl_api import fetch_from_nfl_api
from .fetchers.nflverse import fetch_nfl_events

# 🔀 Merge + Tag + Dashboard
from .merge import merge_events
from .tagging import tag_events
from .dashboard import prepare_dashboard

# 🚀 Unified pipeline
from .fetch import fetch_player_data, run_fetch
from .espn import diagnose_espn_fetch

__all__ = [
    "fetch_player_data",
    "run_fetch",
    "fetch_from_espn",
    "fetch_from_nfl_api",
    "fetch_nfl_events",
    "merge_events",
    "tag_events",
    "prepare_dashboard"
]
