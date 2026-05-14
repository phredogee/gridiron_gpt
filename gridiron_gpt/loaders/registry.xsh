# gridiron_gpt/loaders/registry.xsh — Centralized Loader Registry
import os
from datetime import datetime

PROJECT_ROOT = os.path.expanduser("~/projects/my_project")

def source_loader(path, label):
    full_path = os.path.join(PROJECT_ROOT, path)
    if os.path.isfile(full_path):
        echo(f"📦 Loading {label} → {full_path}")
        source(full_path)
        log_loader(label)
    else:
        echo(f"⚠️ Missing {label} → {full_path}")

def log_loader(label):
    log_path = os.path.join(PROJECT_ROOT, "gridiron_gpt/logs/loader_trace.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] {label} sourced\n")

# 🧠 NLP + Semantic
source_loader("gridiron_gpt/cli_modules/nlp_loader.py", "NLP Loader")
source_loader("gridiron_gpt/semantic/profile_loader.py", "Semantic Profile Loader")

# 🧬 Phred Core
source_loader("gridiron_gpt/phred/shared/phred_loader.py", "Phred Shared Loader")
source_loader("gridiron_gpt/phred/utils/loader.py", "Phred Utils Loader")
source_loader("gridiron_gpt/phredenv/loader.py", "Phredenv Loader")

# 🏈 Sports Pipeline
source_loader("sports_pipeline/loader.py", "Sports Pipeline Loader")
source_loader("sports_pipeline/utils/loader.py", "Sports Pipeline Utils")
