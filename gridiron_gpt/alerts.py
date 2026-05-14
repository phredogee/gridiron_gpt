import os

bot = SlackBot(os.getenv("SLACK_WEBHOOK_URL", ""))
