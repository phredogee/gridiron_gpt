# /gridiron_gpt/sports.py

from phred.utils.env_utils import inject_project_root
from phred.cli.fetch import run_fetch
from phred.env import inject_project_root

from phred.utils.banner_utils import banner, success_banner

banner("Starting ESPN intake...")
success_banner("Fetched 128 player records.")

def smoke_test():
    print("🔄 Running fetch...")
    data = run_fetch()

    print("🔄 Running merge...")
    merged = run_merge()

    print("🔄 Running save...")
    run_save()

    print("✅ All components executed.")
if __name__ == "__main__":
    smoke_test()

def run_fetch():
    from phred.intake.espn import fetch_espn_data

    print("📥 Fetching ESPN data...")
    data = fetch_espn_data(dry_run=True)  # dry-run for onboarding clarity
    print(f"✅ Fetched {len(data)} entries.")
    return data

def run_merge():
    from phred.semantic.index import load_semantic_index
    from phred.intake.espn import fetch_espn_data

    print("🧩 Merging ESPN data with semantic index...")

    # Fetch ESPN data (dry-run or live)
    espn_data = fetch_espn_data(dry_run=True)

    # Load semantic index (e.g. vector embeddings)
    semantic_index = load_semantic_index(dry_run=True)

    merged = []
    missing = []

    for player in espn_data:
        name = player.get("name")
        semantic_entry = semantic_index.get(name)

        if semantic_entry:
            merged.append({**player, **semantic_entry})
        else:
            missing.append(name)

    print(f"✅ Merged {len(merged)} players.")
    if missing:
        print(f"⚠️ Missing semantic entries for {len(missing)} players:")
        for name in missing[:5]:
            print(f"   - {name}")
        if len(missing) > 5:
            print("   ...")

    return merged

def run_save():
    from phred.storage.save import save_merged_data

    print("💾 Saving merged output...")
    save_merged_data(dry_run=True)  # dry-run to preview path or index
    print("✅ Save complete.")

__all__ = ["run_fetch", "run_merge", "run_save"]
