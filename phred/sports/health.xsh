# phred/sports/health.xsh

# 🩺 Health check for fetcher registry and ESPN lazy import
def check_fetch_registry():
    try:
        from phred.sports.fetch_registry import list_fetch_modes, get_fetcher
        modes = list_fetch_modes()
        print("📦 Fetch modes available:", ", ".join(modes))
        for mode in modes:
            fetcher = get_fetcher(mode)
            assert callable(fetcher)
            print(f"✅ Fetcher '{mode}' is callable")
    except Exception as e:
        print(f"❌ Fetch registry check failed: {e}")

# 🧠 Lazy ESPN import test
def check_espn_fetcher():
    try:
        from phred.sports.fetch import FETCHERS
        result = FETCHERS["espn"](season=2024, dry_run=True)
        assert isinstance(result, list)
        print("✅ ESPN fetcher returned dry-run data")
    except Exception as e:
        print(f"❌ ESPN fetcher failed: {e}")

# 🎨 Banner for contributor affirmation
def show_health_banner():
    print("🩺 Running sports module health checks...")
    print("🔍 Validating fetch registry and ESPN diagnostics...\n")

# 🚀 Entry point
def main():
    show_health_banner()
    check_fetch_registry()
    checkFETCHERS ["espn"]()
    print("\n✅ All health checks complete.")

main()
