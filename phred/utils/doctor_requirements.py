# phred/utils/doctor_requirements.py

import importlib

def check_requirements():
    required = ['requests', 'pytest']
    for pkg in required:
        try:
            importlib.import_module(pkg)
            print(f"✅ {pkg} is installed")
        except ImportError:
            print(f"❌ {pkg} is missing")

if __name__ == "__main__":
    check_requirements()
