from .matchup_pipeline import run as run_matchups
from .injury_pipeline import run as run_injuries
from .ranking_pipeline import run as run_rankings
from .news_pipeline import run as run_news
from .projection_pipeline import run as run_projections
from .custom_advice_pipeline import run as run_custom_advice

def build_pipelines():
    print("🔧 Starting pipeline ingestion...")
    run_matchups()
    run_injuries()
    run_rankings()
    run_news()
    run_projections()
    run_custom_advice()
    print("✅ All pipelines ingested.")

if __name__ == "__main__":
    build_pipelines()

    # TODO: Add logic to fetch and embed player-related news
