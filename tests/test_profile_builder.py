# gridiron_gpt/tests/test_profile_builder.py

from phredenv.semantic.profile_builder import build_player_profile

def test_mahomes_profile():
    raw = {
        "name": "Patrick Mahomes",
        "team": "KC",
        "position": "QB",
        "passing_yards": 4820,
        "touchdowns": 41,
        "interceptions": 8,
        "injury_status": None
    }
    profile = build_player_profile(raw, dry_run=True)
    assert "elite" in profile["tags"]
    assert "starter" in profile["tags"]
