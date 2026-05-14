# phred/sports/fetchers/espn/diagnostics.py

from phred.cli.utils.feedback.banner import show_banner, success, warning, error
from phred.sports.fetchers.espn.fetch import fetch_from_espn
from phred.semantic.index import validate_index
import os
import platform

def diagnose_espn_fetch(season="2024", source="espn", dry_run=True):
    show_banner("🩺 ESPN Diagnostics")

    try:
        data = fetch_from_espn(season=season, source=source, dry_run=dry_run)
        if not data or "players" not in data:
            warning("No player data returned. Check source or season.")
        else:
            success(f"Fetched {len(data['players'])} players from {source}.")
    except Exception as e:
        error(f"Fetch failed: {e}")
        suggest("Try running with --verbose or check API keys.")

def diagnose_semantic_index():
    show_banner("🧠 Semantic Index Check")

    try:
        validate_index()
        success("Semantic index is valid and up-to-date.")
    except Exception as e:
        error(f"Index validation failed: {e}")
        suggest("Run `phred doctor --dry-run` to preview index rebuild.")

def diagnose_shell_env():
    show_banner("🐚 Shell & Environment Check")

    shell = os.environ.get("SHELL", "unknown")
    python_path = os.environ.get("VIRTUAL_ENV", "none")
    system = platform.system()

    print(f"🔧 Shell: {shell}")
    print(f"🐍 Virtual Env: {python_path}")
    print(f"🖥️ OS: {system}")

    if shell == "unknown":
        warning("Shell not detected. CLI activation may be shell-sensitive.")
        suggest("Use explicit activation scripts for bash/zsh/fish.")

def suggest(msg: str):
    print(f"💡 Suggestion: {msg}")
