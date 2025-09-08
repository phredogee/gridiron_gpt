#gridiron_gpt/tests/test_cli.py

from phred.sports.fetch import fetch_from_espn

def test_fetch_from_espn_dry_run():
    print("\n📊 ESPN Intake Diagnostic")

    bios = fetch_from_espn(season=2024, dry_run=True)

    # Preview first 5 bios with fallback logic
    for i, p in enumerate(bios[:5], start=1):
        name = p.get("name", "Unnamed")
        team = p.get("team", "Unknown Team")
        position = p.get("position", "Unknown Position")
        print(f"{i}. 🔹 {name} ({team}, {position})")

    # Summary stats
    total = len(bios)
    missing_ids = sum("playerId" not in p for p in bios)
    duplicate_ids = total - len(set(p.get("playerId") for p in bios if "playerId" in p))

    print(f"\n✅ Total bios fetched: {total}")
    if missing_ids:
        print(f"❌ Bios missing playerId: {missing_ids}")
    if duplicate_ids:
        print(f"⚠️ Duplicate playerIds detected: {duplicate_ids}")

    # Assertions
    assert all("playerId" in p for p in bios), "❌ Missing playerId in some bios"
    assert len(set(p["playerId"] for p in bios)) == total, "⚠️ Duplicate playerIds detected"
