def cli_dry_run():
    ctx = ingest_data("data/players.csv", dry_run=True)
    print(ctx.render())
