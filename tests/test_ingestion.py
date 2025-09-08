import pytest
from phred.semantic.ingestion import route_semantic_ingestion
from phred.utils.loader import load_cleaned_data
from phred.utils.splitter import split_matchup

# 🔧 Fixtures
@pytest.fixture
def sample_source():
    return "tests/data/sample_matchup.json"

@pytest.fixture
def sample_identifier():
    return "matchup_001"

@pytest.fixture
def sample_profile():
    return {"normalize": True, "validate": True}

# 🧠 Dry-Run Test
def test_route_ingestion_dry_run(sample_source, sample_identifier, sample_profile, capsys):
    route_semantic_ingestion(sample_source, sample_identifier, sample_profile, dry_run=True)
    captured = capsys.readouterr()
    assert "⚔️ Matchup Diff" in captured.out
    assert "📈" in captured.out or "📉" in captured.out

# 🧼 Data Integrity Test
def test_loaded_data_structure(sample_source, sample_identifier, sample_profile):
    data = load_cleaned_data(sample_source, sample_identifier, sample_profile)
    assert isinstance(data, dict)
    assert "team_a" in data and "team_b" in data

# ⚖️ Matchup Split Test
def test_split_matchup_keys(sample_source, sample_identifier, sample_profile):
    data = load_cleaned_data(sample_source, sample_identifier, sample_profile)
    team_a, team_b = split_matchup(data)
    assert isinstance(team_a, dict)
    assert isinstance(team_b, dict)
    assert set(team_a.keys()) == set(team_b.keys())
