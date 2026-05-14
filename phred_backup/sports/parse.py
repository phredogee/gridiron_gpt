def extract_nfl_events(summary: dict) -> list:
    drives = summary.get("drives", {}).get("previous", [])
    events = []
    for drive in drives:
        for play in drive.get("plays", []):
            events.append({
                "quarter": play.get("quarter"),
                "clock": play.get("clock", {}).get("displayValue"),
                "description": play.get("text"),
                "team": play.get("team", {}).get("shortDisplayName"),
                "type": play.get("type", {}).get("text")
            })
    return events
