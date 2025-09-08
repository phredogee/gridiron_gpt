# feedback.py (formerly banner_utils.py)

def banner(message: str, width: int = 80, emoji: str = "🔔"):
    print("\n" + "═" * width)
    print(f"{emoji} {message}")
    print("═" * width + "\n")

def dry_run_notice():
    banner("Dry-run mode active — no changes will be committed.", emoji="🧪")

def success(message: str):
    banner(f"✅ {message}", emoji="✅")

def warning(message: str):
    banner(f"⚠️ {message}", emoji="⚠️")

def error(message: str):
    banner(f"❌ {message}", emoji="❌")

def onboarding_tip(message: str):
    banner(f"📘 Onboarding Tip: {message}", emoji="📘")
