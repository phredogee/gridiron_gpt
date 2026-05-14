# phred/sports/fetch_registry.py

from .fetch import FETCHERS

def test_fetcher(mode, *args, **kwargs):
    """
    🧪 Runs a dry fetch to validate the fetcher logic.
    """
    try:
        fetcher = get_fetcher(mode)
        result = fetcher(*args, **kwargs)
        print(f"✅ Fetcher '{mode}' executed successfully.")
        return result
    except Exception as e:
        print(f"❌ Fetcher '{mode}' failed: {e}")
        return None

def get_fetcher(mode):
    """
    🎯 Returns the appropriate fetcher function based on mode.
    💡 Valid modes: 'local', 'api', 'scrape', 'espn'
    """
    if mode not in FETCHERS:
        raise ValueError(
            f"❌ Unknown fetch mode: '{mode}'\n"
            f"📦 Valid options: {list(FETCHERS.keys())}"
        )
    return FETCHERS[mode]

def list_fetch_modes():
    """
    📋 Lists all available fetch modes for contributor onboarding.
    """
    return list(FETCHERS.keys())

def show_fetch_banner():
    """
    🎨 Prints a contributor-facing banner of available fetch modes.
    """
    print("📦 Available fetch modes:")
    for mode in FETCHERS:
        print(f"  - {mode} ✅")

def describe_fetcher(mode):
    """
    📚 Prints a short description of the fetcher logic.
    """
    if mode == "espn":
        print("📡 ESPN fetcher uses lazy import to avoid circular dependencies.")
    elif mode == "local":
        print("📁 Local fetcher loads static player data from disk.")
    elif mode == "api":
        print("🌐 API fetcher pulls live data from external services.")
    elif mode == "scrape":
        print("🕷️ Scrape fetcher extracts data from HTML pages.")
    else:
        print("❓ Unknown mode.")

def validate_all_fetchers():
    print("🧪 Validating all fetch modes...")
    for mode in list_fetch_modes():
        describe_fetcher(mode)
        test_fetcher(mode, dry_run=True)

def resolve_mode_alias(alias):
    aliases = {
        "espn": "espn",
        "live": "api",
        "html": "scrape",
        "file": "local"
    }
    return aliases.get(alias, alias)
