from notifier.slack import send_slack_alert

def sunday_alert():
    send_slack_alert("🏈 Sunday kickoff reminder!")

def weather_check():
    send_slack_alert("🌤️ Checking game-day weather conditions")
