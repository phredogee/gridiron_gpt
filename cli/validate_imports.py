# cli/validate_imports.py

def dry_run():
    try:
        from phred.utils.banner_utils import banner
        print("✅ banner_utils import succeeded")
    except ModuleNotFoundError as e:
        print(f"❌ Import failed: {e}")

if __name__ == "__main__":
    dry_run()
