# gridiron_gpt/semantic/intake/store.py

from pathlib import Path
import json

def save_player_data(data, path="player_data.json"):
    """Persist player data to disk."""
    path = Path(path)
    path.write_text(json.dumps(data, indent=2))
    print(f"✅ [store] Saved {len(data)} records to {path}")

def maybe_store_data(data, path="player_data.json", dry_run=False, preview_count=2):
    """
    Store player data unless dry_run is True.
    In dry_run mode, print a preview instead of writing to disk.
    """
    if dry_run:
        print("🛑 [store] Dry-run mode — skipping file write.")
        preview = data[:preview_count] if isinstance(data, list) else str(data)[:200]
        print(f"Preview: {preview} ...")
        return

    save_player_data(data, path)
