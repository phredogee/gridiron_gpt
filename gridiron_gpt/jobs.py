# jobs.py
import logging
from advisor import advisor  # or however you import your pipeline

def incremental_update():
    logging.info("Running incremental update...")
    advisor.update_news()
    advisor.update_injuries()
    logging.info("Incremental update completed.")
