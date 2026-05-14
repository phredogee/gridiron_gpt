# notifier.py

import requests
from gridiron_gpt.app.config import SLACK_WEBHOOK_URL

def notify_slack(message: str):
    if SLACK_WEBHOOK_URL:
        payload = {"text": message}
        try:
            response = requests.post(SLACK_WEBHOOK_URL, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[Slack Error] {e}")
    else:
        print(f"[Slack] {message}")
