from data_pipeline import get_player_stats

if args.source == "nflverse":
    df = get_player_stats([args.season])
    # pass to dashboard or semantic mapper
