# custom_advice_pipeline.py

def fetch_custom_advice():
    # TODO: Replace with manual entries or Google Sheet integration
    return [
        "Start Travis Kelce against the Raiders",
        "Avoid starting Deshaun Watson this week"
    ]

def ingest(advisor):
    texts = fetch_custom_advice()
    embeddings = advisor.embed(texts)
    advisor.add_documents(texts)

from gridiron_gpt.core.advisor import Advisor

def run():
    print("🧠 Running custom advice pipeline...")
    advisor = Advisor()
    ingest(advisor)
    advisor.save_index(advisor.index_path)
    print("📌 Custom advice ingested and index saved.")