# config.py

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"
TRIGGER_ENDPOINT = "http://your-server-ip:5000/run_pipeline"

WATCHED_FILES = {
    "injury_data.csv": "Injury Pipeline",
    "news_feed.json": "News Pipeline",
    "rankings.csv": "Ranking Pipeline"
}
