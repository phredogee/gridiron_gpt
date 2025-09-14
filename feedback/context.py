# phred/feedback/context.py

class FeedbackContext:
    def __init__(self, status):
        self.status = status
        self.logs = []

    def __enter__(self):
        self.log(f"Entering context with status: {self.status}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.log(f"❌ Exception: {exc_val}")
        else:
            self.log(f"✅ Context exited cleanly")

    def log(self, message):
        self.logs.append(message)

    def __str__(self):
        emoji = {
            "success": "✅",
            "warning": "⚠️",
            "error": "❌",
        }.get(self.status, "❓")
        return f"{emoji} " + "\n".join(self.logs)
