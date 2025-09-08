# scripts/dry_run_matchup.py

import sys
from pathlib import Path

# Add gridiron_gpt/ to sys.path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from gridiron_gpt.query import run_query

def run_matchup_query(query: str):
    """Wrapper for run_query, can be extended for matchup-specific logic."""
    return run_query(query)

# Keep ingestion logic for manual runs
if __name__ == "__main__":
    from phred.semantic.matchup_diff import route_semantic_ingestion
    route_semantic_ingestion("espn", "game123", "default")
