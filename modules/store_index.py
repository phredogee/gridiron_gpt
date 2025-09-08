# modules/store_index.py

def store_data(data, path="data/index.json", dry_run=False):
    if dry_run:
        print("🛑 Dry-run mode — skipping actual storage.")
        return
    # Actual save logic goes here

def run_store(clean_data, dry_run=False):
    store_data(clean_data, dry_run=dry_run)
