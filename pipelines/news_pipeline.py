# news_pipeline.py

def fetch_news():
    # TODO: Replace with real RSS, Reddit, or Twitter logic
    return [
        {"headline": "Travis Kelce expected to dominate Raiders"},
        {"headline": "Watson struggles in practice"}
    ]

def format_news_statements(data):
    return [d["headline"] for d in data]

def ingest(advisor):
    raw = fetch_news()
    texts = format_news_statements(raw)
    embeddings = advisor.embed(texts)
    advisor.add_documents(texts, embeddings)

def run():
    print("📰 Running news pipeline...")
    # TODO: Add logic to fetch, format, and embed news data
