# phred/sports/dashboard.py

from collections import defaultdict

def prepare_dashboard(dry_run=False):
    if dry_run:
        print("🧪 Dry-run mode: dashboard generation skipped.")
        return

    # Index bios by playerId
    bio_index = {p["playerId"]: p for p in bios}

    # Group events by player
    player_events = defaultdict(list)
    for e in tagged_events:
        player_events[e["playerId"]].append(e)

    # Build dashboard rows
    dashboard = []
    for pid, events in player_events.items():
        bio = bio_index.get(pid, {})
        row = {
            "playerId": pid,
            "name": bio.get("name", "Unknown"),
            "team": bio.get("team", "Unknown"),
            "position": bio.get("position", "Unknown"),
            "labels": list({e["label"] for e in events}),
            "event_count": len(events),
            "latest_event": max(events, key=lambda e: e["date"])["date"]
        }
        dashboard.append(row)

    print(f"✅ Dashboard ready with {len(dashboard)} players")
    return dashboard

