# gpt/data_ingest/espn_ingest.py

import os
import json
import argparse
import requests
from validators.profile_validator import validate_profile_schema

RAW_DIR = "data/raw/espn"
CLEAN_DIR = "data/clean/espn"

def fetch_espn_data(week: int) -> list:
    """Fetch raw ESPN scoreboard data for a given NFL week."""
    url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week={week}&seasontype=2"
    print(f"📡 Fetching ESPN data for week {week}...")
    response = requests.get(url)
    data = response.json()

    players = []
    for event in data.get("events", []):
        for competitor in event["competitions"][0]["competitors"]:
            team = competitor["team"]["abbreviation"]
            for athlete in competitor.get("athletes", []):
                players.append({
                    "player_name": athlete["displayName"],
                    "team": team,
                    "week": week,
                    "fantasy_points": athlete.get("stats", [{}])[0].get("value", 0),
                    "position": athlete.get("position", {}).get("abbreviation", "UNK")
                })
    return players

def clean_espn_data(raw_data: list) -> list:
    """Transform raw ESPN data into validated profile format."""
    print("🧼 Cleaning ESPN data...")
    cleaned = []
    for entry in raw_data:
        cleaned.append({
            "profile_id": f"{entry['team']}_{entry['player_name'].replace(' ', '_')}",
            "team": entry["team"],
            "week": entry["week"],
            "fantasy_points": float(entry["fantasy_points"]),
            "position": entry.get("position", "unknown")
        })
    print(f"✅ Cleaned {len(cleaned)} player entries")
    return cleaned

def save_cleaned_data(cleaned_data: list, week: int, output_path: str = None):
    """Save cleaned data to disk."""
    os.makedirs(CLEAN_DIR, exist_ok=True)
    path = output_path or os.path.join(CLEAN_DIR, f"week_{week}.json")
    with open(path, "w") as f:
        json.dump(cleaned_data, f, indent=2)
    print(f"💾 Saved cleaned data to {path}")

def banner_feedback(valid: bool, issues: list):
    """Display validation results with expressive feedback."""
    if valid:
        print("✅ ESPN data validated successfully! 🎉")
    else:
        print("🚨 Validation failed:")
        for issue in issues:
            print(f"   ❌ {issue}")

def main():
    parser = argparse.ArgumentParser(description="ESPN NFL Data Ingest Pipeline")
    parser.add_argument("--week", type=int, required=True, help="NFL week number")
    parser.add_argument("--dry-run", action="store_true", help="Preview cleaned data without saving")
    parser.add_argument("--banner", action="store_true", help="Show validation feedback banner")
    parser.add_argument("--output-path", type=str, help="Custom output path for cleaned data")
    args = parser.parse_args()

    raw_data = fetch_espn_data(args.week)
    cleaned_data = clean_espn_data(raw_data)
    valid, issues = validate_profile_schema(cleaned_data)

    if args.banner:
        banner_feedback(valid, issues)

    if args.dry_run:
        print("🧪 Dry-run mode: cleaned data preview")
        print(json.dumps(cleaned_data, indent=2))
    elif valid:
        save_cleaned_data(cleaned_data, args.week, args.output_path)
    else:
        print("⚠️ Data invalid—skipping save")

if __name__ == "__main__":
    main()
