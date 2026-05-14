# phred/__init__.py

# Re-export FeedbackContext from feedback/context.py for CLI and test integration
from .feedback.context import FeedbackContext
from .cli.doctor import run_diagnostics
from phred.sports.espn_diagnostics import diagnose_espn_fetch
from .sports.espn import fetch_from_espn
from .sports.fetch import (
    get_all_player_ids,
    get_player_bios,
    fetch_player_data,
    run_fetch,
    FETCHERS
)

# --- Feedback utilities ---
from .feedback import banner

# --- Semantic ingestion ---
from .semantic.ingestion_core import route_semantic_ingestion
print("🎯 phred package loaded — CLI ecosystem ready for contributors.")

__version__ = "0.1.0"
__all__ = [
    # Sports
    "fetch_from_espn",
    "get_all_player_ids",
    "get_player_bios",
    "fetch_player_data",
    "run_fetch",
    "FETCHERS",
    # Feedback
    "banner",
    "FeedbackContext",
    # Semantic
    "route_semantic_ingestion",
]
