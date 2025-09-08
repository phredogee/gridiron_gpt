# gridiron_gpt/onboarding/onboarding_check.py

import os
from utils.folder_utils import get_clean_path, ensure_folder
from semantic.profile_data import load_cleaned_data
from semantic.profile_delta import compute_profile_delta
from semantic.utils.feedback import banner

def check_cleaned_file(source, profile, identifier):
    path = get_clean_path(source, profile, identifier)
    if not os.path.exists(path):
        banner("❌ Missing Cleaned File")
        print(f"Expected: {path}")
        return False
    banner("✅ Found Cleaned File")
    print(f"Located: {path}")
    return True

def check_semantic_modules(source, profile, identifier):
    try:
        data = load_cleaned_data(source, identifier, profile)
        banner("🧪 Semantic Dry Run")
        delta = compute_profile_delta({"current": data, "previous": {}})
        print(f"Delta sample: {list(delta.items())[:3]}")
    except Exception as e:
        banner("❌ Semantic Module Error")
        print(str(e))

def main():
    source = "espn"
    profile = "QB"
    identifier = "1"

    ensure_folder(f"data/clean/{source}", dry_run=True)
    if check_cleaned_file(source, profile, identifier):
        check_semantic_modules(source, profile, identifier)

if __name__ == "__main__":
    main()
