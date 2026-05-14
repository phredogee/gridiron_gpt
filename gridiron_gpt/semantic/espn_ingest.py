# /gridiron_gpt/semantic/espn_ingest.py

from gridiron_gpt.utils.banner_utils import print_banner
from gridiron_gpt.data_ingest.espn_ingest import fetch_espn_data, clean_espn_data, save_cleaned_data
from gridiron_gpt.validators.profile_validator import validate_profile_schema

def ingest_espn_data(week: int, dry_run: bool = False, banner: bool = False):
    if banner:
        print_banner(f"📦 ESPN Ingest: Week {week}", level="info")

    raw_data = fetch_espn_data(week)
    cleaned_data = clean_espn_data(raw_data)
    valid, issues = validate_profile_schema(cleaned_data)

    if banner:
        if valid:
            print_banner("✅ ESPN data validated successfully!", level="success")
        else:
            print_banner("🚨 Validation failed", level="error")
            for issue in issues:
                print_banner(f"❌ {issue}", level="warn")

    if dry_run:
        print_banner("🧪 Dry-run mode: previewing cleaned data", level="info")
        print(f"\n{cleaned_data[:3]} ...")  # Preview first 3 entries
        return cleaned_data

    if valid:
        save_cleaned_data(cleaned_data, week)
        if banner:
            print_banner("✅ ESPN ingest complete", level="success")
    else:
        if banner:
            print_banner("⚠️ Data invalid—skipping save", level="warn")

    return cleaned_data if dry_run else None

def dry_run_intake(week: int, banner: bool = False):
    print_banner("🧪 Dry-running ESPN ingest", level="info") if banner else None
    data = fetch_espn_data(week)
    cleaned = clean_espn_data(data)
    print(cleaned)
