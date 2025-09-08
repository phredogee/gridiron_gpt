# cli/sports.py

@sports.command()
@click.option('--year', default=2022)
@click.option('--team')
@click.option('--weeks', multiple=True, type=int)
@click.option('--output', default="data/processed/merged_stats.csv")
def merge(year, team, weeks, output):
    player_df = fetch_player_stats(year)
    pbp_df = fetch_pbp_data(year, team=team, weeks=list(weeks))
    merged_df = merge_stats(player_df, pbp_df)
    save_merged_stats(merged_df, path=output)
    print(f"✅ Merged stats saved to {output}")
