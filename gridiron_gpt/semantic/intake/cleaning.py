# intake/cleaning.py

from .store import save_player_data
from .utils.banner_utils import warn_banner

def clean_player_data(data, dry_run=False):
    # 🧹 Add actual cleaning steps here (e.g. normalize columns, filter nulls)
    if dry_run:
        warn_banner("🧪 Dry-run mode: data cleaned but not saved")
    save_player_data(data, dry_run=dry_run)
    return data
