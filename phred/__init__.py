# phred/__init__.py

# --- Sports API ---
from .sports import (
    fetch_from_espn,
    get_all_player_ids,
    get_player_bios,
    fetch_player_data,
    run_fetch,
    FETCHERS
)

# --- Feedback utilities ---
from .feedback import banner, feedback_context

# --- Semantic ingestion ---
from .semantic.ingestion import route_semantic_ingestion

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
    "feedback_context",
    # Semantic
    "route_semantic_ingestion",
]
