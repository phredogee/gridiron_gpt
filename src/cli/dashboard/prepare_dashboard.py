# src/dashboard/prepare_dashboard.py

from typing import List, Dict, Optional

def prepare_dashboard(players: List[Dict], min_confidence: float = 0.6, sort_by: str = "team", dry_run: bool = True) -> Optional[List[Dict]]:
    """
    Filters and organizes player bios for dashboard display.

    Args:
        players (List[Dict]): List of player bios with metadata.
        min_confidence (float): Threshold for bio confidence.
        sort_by (str): Field to sort by ('team', 'position', 'name').
        dry_run (bool): If True, prints preview instead of returning full dashboard.

    Returns:
        Optional[List[Dict]]: Filtered and sorted dashboard-ready bios.
    """
    # Step 1: Filter by confidence
    filtered = [
        p for p in players
        if p.get("confidence", 0) >= min_confidence
    ]

    # Step 2: Sort by field
    sorted_bios = sorted(
        filtered,
        key=lambda p: p.get(sort_by, "")
    )

    # Step 3: Dry-run preview
    if dry_run:
        print(f"🧪 Previewing {len(sorted_bios)} players sorted by '{sort_by}':")
        for p in sorted_bios[:10]:
            print(f"🔹 {p.get('name')} ({p.get('team')}, {p.get('position')}) — {p.get('confidence'):.2f}")
        return None

    # Step 4: Return dashboard data
    return sorted_bios
