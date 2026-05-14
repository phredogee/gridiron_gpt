# gridiron_gpt/modules/utils.py

"""
Used to signal dry-run operations during CLI feedback. 
Helps contributors distinguish between actual execution and simulated output.
"""

import yaml
import os
import logging

logger = logging.getLogger(__name__)

EMOJIS = {
    "info": "ℹ️",
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "debug": "🛠️"
}

def banner(message, level="info"):
    emoji = EMOJIS.get(level, "❓")
    print(f"{emoji} {message}")

def log_dry_run(message: str) -> None:
    """Log a dry-run message with a debug emoji banner."""
    banner(f"[DRY RUN] {message}", level="debug")
    logger.debug(f"[DRY RUN] {message}")

def load_config(path="config/api_keys.yaml"):
    """
    Load API keys from a YAML configuration file.

    Args:
        path (str): Path to the YAML file.

    Returns:
        dict: Parsed key-value pairs from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}")
    logger.info(f"{EMOJIS['info']} Loading config from {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)
