from datetime import datetime
from gridiron_gpt.pipeline import SemanticPipeline
from gridiron_gpt.app.notifier import notify_slack

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
notify_slack(f"🏈 Gridiron_GPT Pipeline ran successfully at {timestamp}")
handle_query("Top 5 WRs against zone coverage", top_n=3)

if __name__ == "__main__":
    print("🏈 Running Gridiron_GPT Pipeline...")
    notify_slack("Gridiron_GPT test message: pipeline ran successfully.")
    
    pipeline = SemanticPipeline()
    matches, index, embeddings = pipeline.run()
    
    print(f"FAISS index size: {index.ntotal if index else 'Index not built'}")
    print(f"First embedding: {embeddings[0][:5] if embeddings else 'No embeddings'}")
    print(f"Semantic matches: {matches if matches else 'No matches found'}")


