# phred/sports/tagging.py

def tag_events(events: list, bios: dict) -> list:
    print("\n🏷️ Tagging semantic labels...")

    def classify(e):
        label = "unknown"
        if "injury" in e["type"].lower():
            label = "injury"
        elif "suspension" in e["type"].lower():
            label = "suspension"
        elif "touchdown" in e["type"].lower() or "breakout" in e["type"].lower():
            label = "breakout"
        elif "retirement" in e["type"].lower() or "milestone" in e["type"].lower():
            label = "milestone"

        # Bonus: check bios for rookie status
        player_bio = bios.get(e["playerId"], {})
        if label == "breakout" and player_bio.get("rookie"):
            label = "rookie_breakout"

        return e | {"label": label}

    tagged = [classify(e) for e in events]
    print(f"✅ Tagged {len(tagged)} events with semantic labels")
    return tagged
