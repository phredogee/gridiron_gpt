# phred/commands/run_pipeline.py

import time
from phred.cli import register_command

@register_command("run-pipeline", help_text="Run the full pipeline with embedding")
def run_pipeline(*args):
    dry_run = "--dry-run" in args
    stages = [fetch_data, preprocess, embed_data, store_results]

    print("🚀 Starting pipeline...")
    for stage in stages:
        stage_name = stage.__name__.replace("_", " ").title()
        print(f"\n🔧 Stage: {stage_name}")
        if dry_run:
            print("🧪 Dry run mode — skipping execution.")
            continue

        start = time.time()
        try:
            stage()
            duration = time.time() - start
            print(f"✅ Completed in {duration:.2f}s")
        except Exception as e:
            print(f"❌ Error in {stage_name}: {e}")
            break

    print("\n🎉 Pipeline finished.")

# 🧩 Stage functions (stubbed for now)
def fetch_data():
    print("📦 Fetching data...")

def preprocess():
    print("🧹 Preprocessing data...")

def embed_data():
    print("🧠 Embedding data...")

def store_results():
    print("🗃️ Storing results...")
