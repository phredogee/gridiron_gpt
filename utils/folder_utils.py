# /gridiron_gpt/utils/folder_utils.py

import os

def ensure_folder(path, dry_run=False):
    if dry_run:
        print(f"🧪 Dry run: would create {path}")
        return
    os.makedirs(path, exist_ok=True)

def get_clean_path(source, profile, identifier):
    return f"data/clean/{source}/{profile}_{identifier}.json"

def compute_profile_delta(profile_data):
    current = profile_data["current"]
    previous = profile_data.get("previous", {})
    return {stat: current.get(stat, 0) - previous.get(stat, 0) for stat in current}
