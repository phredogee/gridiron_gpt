# phred/semantic/audit.py

from .profile_delta import compute_profile_delta
from .profile_loader import load_bios
from pprint import pprint
import json, os

print("🧠 Semantic audit module initialized")

def audit_espn(source: str, dry_run: bool):
    print(f"🔍 Auditing source: {source}")
    if dry_run:
        print("🧪 Dry-run mode active — no changes made.")
    else:
        print("✅ Committing audit results.")
    bios = load_bios(source)

    print(f"📦 Loaded {len(bios)} bios from '{source}'")

    espn_profile = {
        "name": "Justin Jefferson",
        "team": "MIN",
        "position": "WR",
        "age": 25,
        "status": "Active"
    }

    found = False
    for existing_profile in bios:
        if existing_profile.get("position") == "WR":
            found = True
            delta = compute_profile_delta(existing_profile, espn_profile)
            if delta:
                print(f"\n🧠 Semantic Delta for {existing_profile['name']}:")
                pprint(delta)
            else:
                print(f"✅ {existing_profile['name']} matches ESPN profile")

    if not found:
        print("⚠️ No WR profiles found in bios — check source or filter logic")

    if dry_run:
        print("\n🧪 Dry-run mode: no changes made")
    else:
        print("\n✅ Audit complete")

def audit_nflverse(source="all", dry_run=True):
    print("📊 Auditing nflverse stats...")

    bios = load_bios()
    espn_profile = get_espn_profile("WR")  # Stub or mock this as needed

    for existing_profile in bios:
        if existing_profile["position"] == "WR":
            delta = compute_profile_delta(existing_profile, espn_profile)
            pprint(delta)

    if dry_run:
        print("🧪 Dry-run: no changes made")
    else:
        print("✅ Audit complete")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run semantic audit")
    parser.add_argument("--source", choices=["espn", "nflverse"], required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.source == "espn":
        audit_espn(dry_run=args.dry_run)
    elif args.source == "nflverse":
        audit_nflverse(dry_run=args.dry_run)

def test_load_bios_feedback_context():
    bios = load_bios("tests/data/mock_bios.json")
    assert isinstance(bios, list)
    assert all("name" in profile for profile in bios)
