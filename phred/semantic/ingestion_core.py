# phred/semantic/ingestion_core.py

def route_semantic_ingestion(source, identifier, profile, dry_run=False):
    """
    Route the semantic ingestion process.
    In dry-run mode, print matchup diff and trend symbols.
    """
    if dry_run:
        print("⚔️ Matchup Diff")
        print("📈 Simulated upward trend")  # could also be 📉
        return
    # Real ingestion logic would go here
    print("Ingestion complete")


def load_cleaned_data(source, identifier, profile):
    """
    Load cleaned matchup data.
    Returns a dict with 'team_a' and 'team_b' keys.
    """
    return {
        "team_a": {"score": 10, "wins": 5},
        "team_b": {"score": 8, "wins": 4}
    }


def split_matchup(data):
    """
    Split matchup data into two dicts for team_a and team_b.
    Ensures both dicts have the same keys.
    """
    team_a = dict(data.get("team_a", {}))
    team_b = dict(data.get("team_b", {}))
    # Ensure both have the same keys
    all_keys = set(team_a.keys()) | set(team_b.keys())
    for key in all_keys:
        team_a.setdefault(key, None)
        team_b.setdefault(key, None)
    return team_a, team_b
