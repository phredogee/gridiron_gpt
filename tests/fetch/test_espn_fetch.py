# tests/fetch/test_espn_fetch.py

from phred.sports.fetch import get_all_player_ids, fetch_from_espn

def test_get_all_player_ids_dry_run():
    result = get_all_player_ids(season=2024, dry_run=True)
    assert isinstance(result, list)
    assert len(result) > 0
    for player in result:
        assert isinstance(player, dict)
        assert "playerId" in player
        assert "name" in player
        assert "team" in player

def test_fetch_from_espn_dry_run():
    data = fetch_from_espn(season=2024, dry_run=True)
    assert isinstance(data, dict)
    assert "season" in data and data["season"] == 2024
    assert "players" in data and isinstance(data["players"], list)
    assert "count" in data and data["count"] == len(data["players"])
