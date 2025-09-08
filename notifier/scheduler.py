# notifier/scheduler.py

import sys
print(sys.path)
sys.path.append("/home/phredo/projects/my_project")

from apscheduler.schedulers.blocking import BlockingScheduler
from notifier.slack import send_slack_alert
from notifier.jobs.alerts import sunday_alert, weather_check
from notifier.jobs.ingestion import hourly_sync
from notifier.jobs.digest import nightly_digest

scheduler = BlockingScheduler()

scheduler.add_job(sunday_alert, 'cron', day_of_week='sun', hour=9)
scheduler.add_job(weather_check, 'cron', day_of_week='sun', hour=8)
scheduler.add_job(hourly_sync, 'cron', minute=0)
scheduler.add_job(nightly_digest, 'cron', hour=20)

# 🏈 Sunday kickoff reminder
@scheduler.scheduled_job('cron', day_of_week='sun', hour=9)
def sunday_alert():
    send_slack_alert("🏈 Sunday kickoff reminder!")

# 📊 Hourly player data sync
@scheduler.scheduled_job('cron', minute=0)
def hourly_sync():
    run_data_ingestion()
    send_slack_alert("📊 Hourly player data synced")

# 🌤️ Game-day weather check
@scheduler.scheduled_job('cron', day_of_week='sun', hour=8)
def weather_check():
    send_slack_alert("🌤️ Checking game-day weather conditions")

# 📝 Nightly digest summary
@scheduler.scheduled_job('cron', hour=20)
def nightly_digest():
    send_slack_alert("📝 Daily summary: stats, injuries, predictions")

if __name__ == "__main__":
    send_slack_alert("🕒 Scheduler started")
    scheduler.start()
