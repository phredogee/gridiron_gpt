from phred.cli.ranking import generate_rankings

def test_ranking_dry(monkeypatch):
    monkeypatch.setattr("sys.argv", ["phred", "ranking", "--dry-run"])
    rankings = generate_rankings(dry_run=True)
    assert isinstance(rankings, list)
