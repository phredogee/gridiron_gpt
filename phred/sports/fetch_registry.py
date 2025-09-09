# phred/sports/fetch_registry.py

from .fetch import FETCHERS

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
