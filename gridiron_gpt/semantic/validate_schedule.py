# /gridiron_gpt/semantic/validate_schedule.py

from gridiron_gpt.utils.banner_utils import print_banner

def validate_schedule(schedule_data):
    print_banner("🔍 Validating schedule integrity", level="info")

    duplicates = find_duplicate_matchups(schedule_data)
    if duplicates:
        print_banner(f"❌ Found {len(duplicates)} duplicate matchups", level="error")
        for matchup in duplicates:
            print_banner(f"Duplicate: {matchup}", level="warn")
        return False

    print_banner("✅ Schedule validation passed", level="success")
    return True

def find_duplicate_matchups(data):
    seen = set()
    duplicates = []
    for entry in data:
        key = (entry['team1'], entry['team2'], entry['week'])
        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)
    return duplicates
