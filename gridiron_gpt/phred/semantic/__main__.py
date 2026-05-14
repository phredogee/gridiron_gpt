# gpt/phred/semantic/__main__.py
import argparse
from .semantic import SemanticPipeline

def main():
    parser = argparse.ArgumentParser(
        description="Run the SemanticPipeline for player data ingestion and embedding."
    )
    parser.add_argument(
        "--source",
        choices=["local", "api", "scrape"],
        default="local",
        help="Data source to fetch player data from."
    )
    args = parser.parse_args()

    pipeline = SemanticPipeline(source=args.source)
    pipeline.run()

if __name__ == "__main__":
    main()
