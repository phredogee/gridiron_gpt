

def test_fetch_from_espn_dry_run():
    from phred.sports.fetchers.espn import fetch_from_espn
    bios = fetch_from_espn(season=2024, dry_run=True)
    assert isinstance(bios, list)
    assert len(bios) > 0
    assert "name" in bios[0]

print(f"\n✅ Fetched {len(bios)} ESPN bios")
