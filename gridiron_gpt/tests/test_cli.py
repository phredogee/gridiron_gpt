
"""
┌────────────────────────────────────────────┐
│  ESPN Dry-Run Test Map                     │
├────────────┬───────────────────────────────┤
│ Structure  │ data["players"] → list[dict]  │
│ Required   │ Each dict has "playerId"      │
│ Dry-run    │ No fetch, mock bios returned  │
│ Assertions │ No missing or duplicate IDs   │
└────────────┴───────────────────────────────┘
"""
# gridiron_gpt/tests/test_cli.py

import pytest
from phred.cli.espn import fetch_espn_data

@pytest.mark.parametrize("season,limit", [
    (2024, 5),
    (2023, 10),
])
def test_fetch_espn_dry_run(season, limit):
    data = fetch_espn_data(season=season, limit=limit, dry_run=True)

    # Defensive checks
    assert isinstance(data, dict), "Expected dict from fetch_espn_data"
    assert "players" in data, "Missing 'players' key in response"
    bios = data["players"]
    assert isinstance(bios, list), "Expected list of player bios"

    # Basic assertions
    missing_ids = [p for p in bios if "playerId" not in p]
    assert not missing_ids, f"Bios missing playerId: {len(missing_ids)}"

    ids = [p["playerId"] for p in bios if "playerId" in p]
    assert len(ids) == len(set(ids)), "Duplicate playerIds found"

    # Optional preview
    for i, p in enumerate(bios[:5], start=1):
        name = p.get("name", "Unnamed")
        team = p.get("team", "Unknown Team")
        position = p.get("position", "Unknown Position")
        print(f"{i}. 🔹 {name} ({team}, {position})")

    print(f"\n✅ Total bios fetched: {len(bios)}")
    if missing_ids:
        print(f"❌ Bios missing playerId: {len(missing_ids)}")
    if len(ids) != len(set(ids)):
        print(f"⚠️ Duplicate playerIds detected")
