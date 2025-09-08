from notifier.slack import send_slack_alert

def nightly_digest():
    send_slack_alert("📝 Daily summary: stats, injuries, predictions")
