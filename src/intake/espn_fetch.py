# src/intake/espn_fetch.py

from merge.validate_merge import validate_merge
from index.semantic_index import load_index  # assuming this loads your embedding index

def fetch_espn_data(dry_run=True):
    # Your existing ESPN fetch logic
    espn_data = [...]  # fetched player dicts

    if dry_run:
        print("\n🔍 Running dry-merge diagnostics...")
        semantic_index = load_index()
        validate_merge(espn_data, semantic_index)

    return espn_data
