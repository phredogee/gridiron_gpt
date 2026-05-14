@register_command("run-pipeline")
def run_pipeline():
    print("🚀 Running sports pipeline...")
    player_data = fetch_player_stats()
    print("🔍 Fetching player stats...")
    pbp_data = fetch_play_by_play("401585932")  # Example game ID
    print("📊 Fetching play-by-play data...")
    merged = merge_stats(player_data, pbp_data)
    print("🧩 Merging stats...")
    save_merged_stats(merged)
    print("💾 Saving merged stats...")
