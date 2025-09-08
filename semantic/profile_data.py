# gridiron_gpt/semantic/profile_data.py

import os
import json

def run_semantic_cli(source="espn", profile="player", identifier="2025", dry_run=False):
    data = load_cleaned_data(source, profile, identifier, dry_run=dry_run)
    if dry_run:
        print("🧪 Dry-run: semantic CLI loaded data preview")
        print(data)
    else:
        print("✅ Semantic CLI loaded data")

def get_clean_path(source, profile, identifier):
    """Constructs the path to the cleaned profile data file."""
    return f"data/{source}/{profile}/{identifier}_cleaned.json"

def load_snapshot(source, profile, identifier):
    """Loads the previous snapshot of cleaned profile data."""
    prev_id = str(int(identifier) - 1)
    path = get_clean_path(source, profile, prev_id)
    if not os.path.exists(path):
        print(f"⚠️ Snapshot not found at {path}")
        return {}
    with open(path, "r") as f:
        print(f"📂 Loaded snapshot from {path}")
        return json.load(f)

def load_cleaned_data(source, profile, identifier, dry_run=False):
    """Loads the current cleaned profile data."""
    path = get_clean_path(source, profile, identifier)
    if dry_run:
        print(f"🧪 Dry-run: would load cleaned data from {path}")
        return {}
    if not os.path.exists(path):
        print(f"⚠️ Cleaned data not found at {path}")
        return {}
    with open(path, "r") as f:
        print(f"📂 Loaded cleaned data from {path}")
        return json.load(f)

def compute_profile_delta(profile_data):
    """Computes the delta between current and previous profile stats."""
    current = profile_data.get("current", {})
    previous = profile_data.get("previous", {})
    return {
        stat: current.get(stat, 0) - previous.get(stat, 0)
        for stat in current
    }
