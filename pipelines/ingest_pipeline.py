# gpt/pipelines/ingest_pipeline.py

"""
✅ Always pass structured data (list of dicts) to embedding functions
✅ Use a loader for .jsonl files before embedding
✅ Label the source for diagnostics and contributor clarity
🚫 Don’t pass filenames directly to embedding functions—they expect data, not paths
"""

from fetch.nfl_api import fetch_players
from preprocess.normalize import normalize_names
from preprocess.fill_missing import fill_missing_stats
from store.to_jsonl import save_to_jsonl
from embed.vectorize import embed_profiles
import json

def load_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(line) for line in f]

def run_pipeline():
    raw = fetch_players()
    normalized = normalize_names(raw)
    filled = fill_missing_stats(normalized)
    save_to_jsonl(filled, "players.jsonl")

    profiles = load_jsonl("players.jsonl")
    embed_profiles(profiles, source="jsonl")
