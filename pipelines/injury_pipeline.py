# injury_pipeline.py

def fetch_injury_data():
    # TODO: Replace with real API or scraping logic
    return [
        {"player": "Joe Burrow", "status": "Questionable", "note": "Calf strain"},
        {"player": "Saquon Barkley", "status": "Healthy", "note": ""}
    ]

def format_injury_statements(data):
    return [f"{d['player']} is {d['status']}. {d['note']}" for d in data]

from project_gridiron_gpt.core.advisor import Advisor

def ingest(advisor):
    # Simulated injury data — later replace with real ingestion logic
    injury_texts = [
        "Christian McCaffrey is questionable with a calf strain.",
        "Joe Burrow is out for the season with a wrist injury.",
        "Tyreek Hill is expected to play despite a minor ankle tweak.",
        "Travis Kelce missed Wednesday’s walkthrough."
    ]

    advisor.add_documents(injury_texts)

def run():
    advisor = Advisor()
    ingest(advisor)
    advisor.save_index(advisor.index_path)
    print("🚑 Injury data ingested and index saved.")
