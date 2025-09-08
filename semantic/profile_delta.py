# semantic/audit.py

import json
import os
from collections import defaultdict

def load_team_profile(team_id: str) -> dict:
    # your logic here
    return profile_data

# 🔧 Utility: Load cleaned data
def load_cleaned_data(source, identifier, profile):
    path = f"data/clean/{source}/{profile}_{identifier}.json"
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ No cleaned data found at {path}")
    with open(path, "r") as f:
        return json.load(f)

# 📊 Core: Compute profile delta
def compute_profile_delta(existing, incoming):
    delta = {}

    for key in incoming:
        if key not in existing:
            delta[key] = f"🆕 Missing in baseline: {incoming[key]}"
        elif existing[key] != incoming[key]:
            delta[key] = {
                "baseline": existing[key],
                "incoming": incoming[key],
                "note": f"⚠️ Mismatch in '{key}'"
            }

    return delta

# 🧠 Semantic Routing
def route_semantic_ingestion(source, identifier, profile):
    incoming = load_cleaned_data(source, identifier, profile)
    existing = load_team_profile(profile)  # 🧠 Load baseline profile

    delta = compute_profile_delta(existing, incoming)
    return delta

    position = profile.upper()
    grouped = defaultdict(list)

    for entry in data:
        profile_id = entry.get("profile_id", "unknown")
        team = entry.get("team", "unknown")
        week = entry.get("week", "unknown")
        points = entry.get("fantasy_points", 0)

        if position in profile_id:
            grouped[profile_id].append({
                "team": team,
                "week": week,
                "fantasy_points": points
            })

    if not grouped:
        return f"⚠️ No profiles found for position '{position}'"

    summary = {}
    for pid, entries in grouped.items():
        total = sum(e["fantasy_points"] for e in entries)
        avg = round(total / len(entries), 2)
        summary[pid] = {
            "games": len(entries),
            "total_points": total,
            "avg_points": avg
        }

    return summary

# 🧪 Audit: ESPN
def audit_espn(source="all", dry_run=True):
    try:
        from semantic.profile_delta import compute_profile_delta
    except ImportError as e:
        print(f"🌀 Circular import detected: {e}")
