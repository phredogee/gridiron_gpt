# ranking_pipeline.py
from data_sources.rankings import fetch_rankings

def format_ranking_statements(data):
    return [f"{d['player']} is ranked #{d['rank']} this week." for d in data]

def ingest(advisor):
    raw = fetch_rankings()
    texts = format_ranking_statements(raw)
    embeddings = advisor.embed(texts)
    return texts, embeddings

def run_pipeline_logic(pipeline_type, data=None, advisor=None):
    if pipeline_type == "ranking":
        print("Running ranking pipeline")
        if advisor:
            texts, embeddings = ingest(advisor)
            advisor.add_documents(texts, embeddings)
        else:
            print("Missing advisor for ranking pipeline.")
    
    elif pipeline_type == "injury":
        from pipelines.injury_pipeline import run
        return run(data)
    
    else:
        raise ValueError(f"Unknown pipeline type: {pipeline_type}")

def run(*args, **kwargs):
    return run_pipeline_logic(*args, **kwargs)

def fetch_rankings():
    return [
        {"player": "Justin Jefferson", "rank": 1},
        {"player": "Ja'Marr Chase", "rank": 2},
        {"player": "Tyreek Hill", "rank": 3},
    ]
