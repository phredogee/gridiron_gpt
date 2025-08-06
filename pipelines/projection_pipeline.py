# projection_pipeline.py
from project_gridiron_gpt.core.advisor import Advisor


def fetch_projections():
    # TODO: Replace with real API or spreadsheet logic
    return [
        {"player": "Jalen Hurts", "projection": "25.3 points"},
        {"player": "Nick Chubb", "projection": "18.7 points"}
    ]

def format_projection_statements(data):
    return [f"{d['player']} is projected to score {d['projection']}." for d in data]

def ingest(advisor):
    raw = fetch_projections()
    texts = format_projection_statements(raw)
    embeddings = advisor.embed(texts)
    advisor.add_documents(texts, embeddings)

def run():
    print("📈 Running projection pipeline...")
    # TODO: Add logic to fetch, process, and embed projection data
    print("✅ Projection pipeline complete.")

def ingest(advisor):
    projection_texts = [
        "Bijan Robinson is projected to score 18.4 fantasy points in Week 1.",
        "Jalen Hurts is expected to throw for 2 touchdowns and rush for 1.",
        "Justin Jefferson is projected for 120 receiving yards and a TD.",
        "Tony Pollard has a favorable matchup against the Giants' run defense."
    ]

    advisor.add_documents(projection_texts)

def run():
    advisor = Advisor()
    ingest(advisor)
    advisor.save_index(advisor.index_path)
    print("📈 Projection pipeline complete.")