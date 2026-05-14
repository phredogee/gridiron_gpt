# interface/commands/schedule.py

import typer
from notifier import scheduler

app = typer.Typer()

@app.command()
def run():
    """Trigger scheduled jobs manually."""
    scheduler.send_slack_alert("🕒 CLI-triggered scheduler start")
    scheduler.scheduler.start()

@app.command()
def list_jobs():
    """List all scheduled jobs."""
    jobs = scheduler.scheduler.get_jobs()
    if not jobs:
        print("⚠️ No jobs scheduled.")
        return
    for job in jobs:
        print(f"🔹 {job.name} — next run: {job.next_run_time}")
        if verbose:
            print(f"   ↪ ID: {job.id}, Trigger: {job.trigger}, Args: {job.args}")
