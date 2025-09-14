# cli/validate_imports.py

def dry_run():
    checks = [
        ("phred.utils.banner_utils", "banner"),
        ("phred.feedback", "FeedbackContext"),
    ]
    for module_path, symbol in checks:
        try:
            exec(f"from {module_path} import {symbol}")
            print(f"✅ {symbol} from {module_path} import succeeded")
        except ModuleNotFoundError as e:
            print(f"❌ Import failed: {e}")

if __name__ == "__main__":
    dry_run()
