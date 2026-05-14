import requests
import json

class SlackBot:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_message(self, text: str):
        payload = {
            "text": text,
            "mrkdwn": True  # Enables Markdown formatting
        }
        response = requests.post(
            self.webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        print(f"[SlackBot] Status: {response.status_code}")

        # You can later add actual HTTP POST logic here
