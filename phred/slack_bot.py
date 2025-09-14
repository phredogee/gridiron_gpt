
class SlackBot:
    def __init__(self, *args, **kwargs):
        print("🧪 Stub SlackBot initialized")

    def send_message(self, text):
        print(f"📨 Stub SlackBot would send: {text}")
        return True

    def notify(self, channel, message):
        print(f"🔔 Stub SlackBot notify: {channel} → {message}")
        return True
