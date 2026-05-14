

"""
📦 sports_pipeline.loader
Core orchestrator for pipeline startup, config loading, and data hooks.
"""

import os
import sys
import logging
from pathlib import Path

# Optional: YAML config support
try:
    import yaml
except ImportError:
    yaml = None  # fallback or raise later

# 🧼 Session guard
if getattr(sys.modules[__name__], "__LOADED__", False):
    print("⚠️ loader.py already initialized. Skipping re-run.")
    raise SystemExit
else:
    setattr(sys.modules[__name__], "__LOADED__", True)

# 📣 Banner
print("🚀 sports_pipeline.loader initializing...")

# 🗂️ Paths
ROOT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = ROOT_DIR / "config.yaml"

# 🧠 Config loader
def load_config(path=CONFIG_PATH):
    if not yaml:
        raise ImportError("PyYAML not installed. Cannot load config.")
    if not path.exists():
        print(f"⚠️ Config file not found at {path}")
        return {}
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    print("✅ Config loaded.")
    return config

# 🏈 ESPN or nflverse stub
def init_data_sources(config):
    print("📡 Initializing data sources...")
    # Stub: Replace with actual ESPN/nflverse logic
    if config.get("use_espn"):
        print("🔌 ESPN API hook enabled.")
    if config.get("use_nflverse"):
        print("📊 nflverse pipeline enabled.")
    print("✅ Data sources initialized.")

# 🧩 Entrypoint
def main():
    config = load_config()
    init_data_sources(config)
    print("🎯 sports_pipeline.loader complete.")

# Optional: CLI entry
if __name__ == "__main__":
    main()
