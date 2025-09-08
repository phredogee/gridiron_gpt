from phred.semantic.ingest import ingest_data

def test_ingest_sample():
    sample = {"team": "Texans", "score": 27}
    result = ingest_data(sample)
    assert result["team"] == "Texans"
