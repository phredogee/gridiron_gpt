# slack_notifier.py

import requests
from .config import SLACK_WEBHOOK_URL = https://hooks.slack.com/services/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, TRIGGER_ENDPOINT = "https://702b6531f5b3.ngrok-free.app/run_pipeline"

def send_pipeline_alert(filename, pipeline_name):
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📄 New file detected: `{filename}`\nTrigger *{pipeline_name}*?"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Run Now"
                        },
                        "url": TRIGGER_ENDPOINT
                    }
                ]
            }
        ]
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    return response.status_code
