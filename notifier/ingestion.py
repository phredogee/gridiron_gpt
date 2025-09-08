from notifier.slack import send_slack_alert
from pipeline.ingest import run_data_ingestion

def hourly_sync():
    run_data_ingestion()
    send_slack_alert("📊 Hourly player data synced")
