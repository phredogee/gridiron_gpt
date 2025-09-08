from phred.cli.espn import fetch_espn_data

def test_espn_fetch_dry(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "espn", "--season", "2024", "--limit", "1", "--dry-run"])
    data = fetch_espn_data(season="2024", limit=1, dry_run=True)
    assert isinstance(data, dict)
    assert "dry_run" in data
