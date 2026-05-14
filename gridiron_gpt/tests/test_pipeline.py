# tests/test_pipeline.py

"""
┌────────────────────────────────────────────┐
│  Pipeline Test Map                         │
├────────────┬───────────────────────────────┤
│ dry_run    │ Prints diagnostic message     │
│ advisor    │ Must expose add_documents     │
│ pipeline   │ Should return structured data │
└────────────┴───────────────────────────────┘

┌────────────────────┬──────────────────────────────┬────────────────────────────┐
│   pipeline_name    │     Dry-Run Output           │     Full Execution Output  │
├────────────────────┼──────────────────────────────┼────────────────────────────┤
│ "ranking"          │ 🧪 Running in dry-run mode   │ ✅ Ranked data returned    │
│ "ingestion"        │ 🧪 Dry-run: no data loaded   │ ✅ Data ingested           │
│ "feedback"         │ ℹ️ Feedback diagnostics only │ ✅ Feedback appliedd          
│ "espn"             │ 🧪 ESPN fetch skipped        │ ✅ Data fetched from ESPN  │
└────────────────────┴──────────────────────────────┴────────────────────────────┘

"""
# 🧪 Onboarding Tip:
# ✅ Always import the function you're testing—even if it's used in other modules
# ✅ Keep test imports grouped and explicit for clarity
# ✅ Use dry-run mode to validate structure without hitting live endpoints

import pytest
from gridiron_gpt.core.advisor import Advisor
from pipelines.ranking_pipeline import run_pipeline_logic
from phred.sports.espn import fetch_from_espn
from gridiron_gpt.data_pipeline import (
    load_play_by_play,
    load_player_stats,
    load_team_stats
)

def test_play_by_play():
    pbp = load_play_by_play()
    assert not pbp.empty
    print("✅ Play-by-play data loaded.")

def test_player_stats():
    stats = load_player_stats()
    assert not stats.empty
    print("✅ Player stats loaded.")

def test_team_stats():
    teams = load_team_stats()
    assert not teams.empty
    print("✅ Team stats loaded.")

def test_advisor_instantiation():
    advisor = Advisor()
    assert advisor is not None
    print("✅ Advisor instantiated.")

if __name__ == "__main__":
    test_play_by_play()
    test_player_stats()
    test_team_stats()

# Optional introspection diagnostics
def test_pipeline():
    result = run_pipeline_logic(season=2024, dry_run=True)
    assert result["season"] == 2024
    assert isinstance(result["rankings"], list)
    assert result["count"] == len(result["rankings"])

def test_advisor_introspection():
    advisor = Advisor()
    print("Advisor class:", advisor.__class__)
    print("Advisor method args:", advisor.add_documents.__code__.co_varnames)
    print("Method:", advisor.add_documents)
    print("Method type:", type(advisor.add_documents))
    assert callable(advisor.add_documents)

def test_pipeline_dry_run_output(capsys):
    run_pipeline_logic(season=2024, dry_run=True)
    captured = capsys.readouterr()
    assert "Dry-run mode: using stubbed ESPN data" in captured.out

def test_pipeline_execution_stub():
    try:
        run_pipeline_logic(season=2024, dry_run=False)
    except NotImplementedError as e:
        assert "Live ESPN fetch" in str(e)

@pytest.mark.parametrize("season,expected_log", [
    (2024, "Dry-run mode: using stubbed ESPN data"),
    (2023, "Dry-run mode: using stubbed ESPN data"),  # same stubbed output
])
def test_pipeline_dry_run_behavior(season, expected_log, capsys):
    run_pipeline_logic(season=season, dry_run=True)
    captured = capsys.readouterr()
    assert expected_log in captured.out
