def fetch_matchup_data():
    # TODO: Replace with real API or scraping logic
    return [
        {"team": "Chiefs", "opponent": "Raiders"},
        {"team": "49ers", "opponent": "Seahawks"}
    ]

def format_matchup_statements(data):
    return [f"{d['team']} are playing against the {d['opponent']} this week." for d in data]

def ingest(advisor):
    raw = fetch_matchup_data()
    texts = format_matchup_statements(raw)
    embeddings = advisor.embed(texts)
    advisor.add_documents(texts, embeddings)

def run():
    # This is the standardized entry point for builder.py
    raw = fetch_matchup_data()
    return format_matchup_statements(raw)
