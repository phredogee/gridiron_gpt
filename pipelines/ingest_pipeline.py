# gpt/pipelines/ingest_pipeline.py

from fetch.nfl_api import fetch_players
from preprocess.normalize import normalize_names
from preprocess.fill_missing import fill_missing_stats
from store.to_jsonl import save_to_jsonl
from embed.vectorize import embed_profiles

def run_pipeline():
    raw = fetch_players()
    normalized = normalize_names(raw)
    filled = fill_missing_stats(normalized)
    save_to_jsonl(filled, "players.jsonl")
    embed_profiles("players.jsonl")

