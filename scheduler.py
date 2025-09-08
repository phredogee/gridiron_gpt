from gridiron_gpt.core.advisor import Advisor
from gridiron_gpt.pipelines import (
    matchup_pipeline,
    injury_pipeline,
    ranking_pipeline,
    news_pipeline,
    projection_pipeline,
    custom_advice_pipeline
)
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging

advisor = Advisor()

# Replace these with your actual ingestion functions
def full_ingestion():
    logging.info("Running full ingestion...")
    # advisor.clear_index()
    # advisor.ingest(...)
    # advisor.save_index(...)

def incremental_update():
    logging.info("Running incremental update...")
    # advisor.ingest(...)
    # advisor.save_index(...)
    
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

scheduler = BackgroundScheduler()
scheduler.add_job(full_ingestion, 'interval', minutes=1)
scheduler.add_job(incremental_update, 'interval', minutes=15)
scheduler.start()

logging.info("Scheduler started. Waiting for jobs...")

# Keep the script running
try:
    while True:
        time.sleep(60)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    logging.info("Scheduler shut down.")
