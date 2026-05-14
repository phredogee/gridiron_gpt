from notifier import scheduler

def run_schedule(args):
    scheduler.send_slack_alert("🕒 CLI-triggered scheduler start")
    scheduler.scheduler.start()

def register(subparsers):
    parser = subparsers.add_parser("schedule", help="Start the scheduler")
    parser.set_defaults(func=run_schedule)
