# tests/fetch/test_espn_fetch.py

from phred.sports.espn import get_all_player_ids, fetch_from_espn

def test_get_all_player_ids_dry_run():
    result = get_all_player_ids(season=2024, dry_run=True)
    print(f"✅ Retrieved {len(result)} player IDs for season 2024")
    assert isinstance(result, list)
    assert len(result) > 0
    for i, player in enumerate(result, start=1):
        assert "playerId" in player, f"❌ Missing playerId in entry {i}"
        assert isinstance(player, dict)
        assert "playerId" in player
        assert "name" in player
        assert "team" in player

def test_fetch_from_espn_dry_run():
    data = fetch_from_espn(season=2024, dry_run=True)
    print("\n🧪 Running test_get_all_player_ids_dry_run...")
    assert isinstance(data, dict)
    assert "season" in data and data["season"] == 2024
    assert "players" in data and isinstance(data["players"], list)
    assert "count" in data and data["count"] == len(data["players"])
