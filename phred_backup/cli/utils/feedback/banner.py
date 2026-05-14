# phred/cli/utils/feedback/banner.py

def show_banner(msg: str):
    print(f"\n🌟 {msg}\n")

def success(msg: str):
    print(f"✅ {msg}")

def warning(msg: str):
    print(f"⚠️ {msg}")

def error(msg: str):
    print(f"❌ {msg}")
