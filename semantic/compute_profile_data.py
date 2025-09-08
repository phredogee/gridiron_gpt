def compute_profile_delta(existing, incoming):
    """
    Compare two player profiles and return semantic deltas.
    - Flags missing fields
    - Highlights mismatches
    - Ignores matching fields
    """
    delta = {}

    for key in incoming:
        if key not in existing:
            delta[key] = f"🆕 Missing in baseline: {incoming[key]}"
        elif existing[key] != incoming[key]:
            delta[key] = {
                "baseline": existing[key],
                "incoming": incoming[key],
                "note": f"⚠️ Mismatch in '{key}'"
            }

    return delta
