# reset.py 🧠
import os
from datetime import datetime

def log_reset():
    print(f"📅 Reset triggered at {datetime.now().isoformat()}")

def validate_project_structure(root):
    expected = ["shell", "phredenv", "modules"]
    missing = [d for d in expected if not os.path.isdir(os.path.join(root, d))]
    if missing:
        print(f"⚠️ Missing folders: {', '.join(missing)}")
    else:
        print("✅ Project structure looks good.")

def run_reset():
    log_reset()
    root = os.environ.get("PHRED_PROJECT_ROOT", ".")
    validate_project_structure(root)
    print("🔧 Environment reset complete.")
