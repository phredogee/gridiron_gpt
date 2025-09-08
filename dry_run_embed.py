# /gpt/dry_run_embed.py

def test_dry_run_embedding():
    players = ["bijan", "gibbs"]
    metrics = ["snap_share", "red_zone_touches", "target_share"]

    print("🧪 Dry-run mode: no data will be written.")
    print(f"👤 Players: {players}")
    print(f"📊 Metrics: {metrics}")

    # Simulate embedding logic here
    assert isinstance(players, list)
    assert "bijan" in players
