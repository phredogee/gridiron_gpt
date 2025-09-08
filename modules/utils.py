import yaml
import os

def load_config(path="config/api_keys.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)
