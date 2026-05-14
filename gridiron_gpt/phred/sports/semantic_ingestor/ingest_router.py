# semantic_ingestor/ingest_router.py

from sources.espn_ingest import fetch_espn_data
from sources.nflverse_ingest import fetch_nflverse_data
from normalizers.profile_mapper import map_to_semantic_profile, map_nflverse_profile

def ingest(source: str, url_or_season, dry_run: bool = False, position: str = None):
    if source == "espn":
        raw = fetch_espn_data(url_or_season)
        profiles = map_to_semantic_profile(raw, source)
    elif source == "nflverse":
        raw = fetch_nflverse_data(url_or_season, position)
        profiles = map_nflverse_profile(raw)
    else:
        raise ValueError(f"❌ Unknown source: {source}")

    if dry_run:
        print(f"🧪 Dry-run: {len(profiles)} profiles parsed from {source}")
    return profiles
