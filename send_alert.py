from datetime import datetime
from notifier.slack import send_slack_alert

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
send_slack_alert(f"🏈 Alert triggered at {timestamp}")
