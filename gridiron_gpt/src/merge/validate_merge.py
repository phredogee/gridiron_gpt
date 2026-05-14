# src/merge/validate_merge.py

from difflib import get_close_matches

def fuzzy_lookup(name, index, cutoff=0.85):
    matches = get_close_matches(name, index.keys(), n=1, cutoff=cutoff)
    return matches[0] if matches else None

def is_ambiguous(name, index):
    matches = get_close_matches(name, index.keys(), n=3, cutoff=0.75)
    return len(matches) > 1

def validate_merge(espn_data, semantic_index):
    summary = {"matched": 0, "missing": 0, "ambiguous": 0}
    for player in espn_data:
        name = player["name"]
        match = fuzzy_lookup(name, semantic_index)
        if not match:
            print(f"🔴 Missing: {name}")
            summary["missing"] += 1
        elif is_ambiguous(name, semantic_index):
            print(f"🟡 Ambiguous: {name} → {match}")
            summary["ambiguous"] += 1
        else:
            print(f"🟢 Match: {name} → {match}")
            summary["matched"] += 1

    print(f"\n✅ Summary: {summary['matched']} matched | 🔴 {summary['missing']} missing | 🟡 {summary['ambiguous']} ambiguous")
