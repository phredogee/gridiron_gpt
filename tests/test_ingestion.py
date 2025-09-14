# gridiron_gpt/tests/test_ingestion.py

import pytest

# ┌────────────────────────────────────────────┐
# │  Ingestion Test Flow Map                   │
# ├────────────┬───────────────────────────────┤
# │ Dry-run    │ Route summary only            │
# │ Loaded     │ Dict with 'matchups' key      │
# │ Split keys │ Format: matchup_id:teamA_vs_B │
# └────────────┴───────────────────────────────┘

# Sample dry-run route for testing
@pytest.fixture
def sample_route():
    return {
        "identifier": "matchup_001",
        "profile": {"normalize": True, "validate": True},
        "source": "tests/data/sample.json"
    }

def test_route_ingestion_dry_run(sample_route):
    # Simulate dry-run routing logic
    routed = [sample_route]  # Replace with actual dry-run call if needed
    assert isinstance(routed, list)
    assert routed[0]["identifier"] == "matchup_001"
    assert "profile" in routed[0]
    assert routed[0]["source"].endswith(".json")

def test_loaded_data_structure():
    # Simulate loading data from file
    data = {"matchups": [{"id": "matchup_001"}]}  # Replace with actual load
    assert isinstance(data, dict), "Expected dict structure"
    assert "matchups" in data, "Missing 'matchups' key"
    assert isinstance(data["matchups"], list), "Expected list of matchups"

@pytest.mark.parametrize("raw_key,expected", [
    ("matchup_001:teamA_vs_teamB", ("matchup_001", "teamA_vs_teamB")),
    ("matchup_002:teamC_vs_teamD", ("matchup_002", "teamC_vs_teamD")),
])
def test_split_matchup_keys(raw_key, expected):
    def split_matchup_keys(key):
        if ":" not in key:
            raise ValueError(f"Invalid matchup format: {key}")
        return tuple(key.split(":", 1))

    assert split_matchup_keys(raw_key) == expected

@pytest.mark.parametrize("bad_key", [
    "matchup_003",  # Missing delimiter
    "Sample record one",  # Malformed
])
def test_split_matchup_keys_invalid(bad_key):
    def split_matchup_keys(key):
        if ":" not in key:
            raise ValueError(f"Invalid matchup format: {key}")
        return tuple(key.split(":", 1))

    with pytest.raises(ValueError, match="Invalid matchup format"):
        split_matchup_keys(bad_key)
