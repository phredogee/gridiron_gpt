# ingest.py
from core.advisor import Advisor
from pipelines import (
    matchup_pipeline,
    injury_pipeline,
    ranking_pipeline,
    news_pipeline,
    projection_pipeline,
    custom_advice_pipeline
)

def run_all_ingestions():
    advisor = Advisor()

    for pipeline in [
        matchup_pipeline,
        injury_pipeline,
        ranking_pipeline,
        news_pipeline,
        projection_pipeline,
        custom_advice_pipeline
    ]:
        print(f"Ingesting from {pipeline.__name__}...")
        pipeline.ingest(advisor)

    advisor.save_index("index_store/faiss_index.bin")
    print("✅ FAISS index saved.")

if __name__ == "__main__":
    run_all_ingestions()
