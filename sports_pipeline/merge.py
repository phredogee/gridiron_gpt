def save_merged_stats(df, path="data/processed/merged_stats.csv"):
    df.to_csv(path, index=False)
