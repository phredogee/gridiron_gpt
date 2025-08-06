# interface/cli.py

import os
import argparse
from project_gridiron_gpt.app.advisor import build_advisor

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run GridironGPT advisor")
    parser.add_argument("--query", type=str, help="Query for semantic advice")
    parser.add_argument("--rebuild", action="store_true", help="Force rebuild the index")
    parser.add_argument("--ingest", action="store_true", help="Run full ingestion pipeline")
    args = parser.parse_args()
    
    advisor = build_advisor()
    print("CLI is working!")

    # 🧠 Ingest pipeline
    if args.ingest:
        advisor.ingest()

    # 🧼 Rebuild index if requested
    if args.rebuild:
        advisor.rebuild_index(save_path="index_rebuilt.index")

    index_path = "index_rebuilt.index" if args.rebuild else "index_rebuilt.index"
    if os.path.exists(index_path):
        advisor.load_index()
        response = advisor.query("Should I start Dalton Kincaid in PPR?")
    else:
        print(f"⚠️ Index file not found: {index_path}. Run with --ingest or --rebuild.")
        return

    # 🔍 Run semantic query
    if args.query:
        results = advisor.advise(args.query)
        for r in results:
            print(f"{r['text']} (score: {r['score']:.2f})")
    elif not (args.ingest or args.rebuild):
        print("No action provided. Use --query, --ingest, or --rebuild.")
        print("Example: python -m interface.cli --query 'Who should I start at RB?'")
    
if __name__ == "__main__":
    main()