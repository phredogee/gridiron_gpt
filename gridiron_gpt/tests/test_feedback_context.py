# tests/test_feedback_context.py

from phred.feedback.context import FeedbackContext

def test_emit_success_message():
    with FeedbackContext("success") as ctx:
        ctx.log("Operation completed")
        assert "✅" in str(ctx)

def test_dry_run_logging():
    ctx = FeedbackContext("debug", dry_run=True)
    ctx.debug("Dry run test message")
    assert "DRY-RUN DEBUG: Dry run test message" in ctx.render()

def test_feedback_context_basic():
    with FeedbackContext("success") as ctx:
        ctx.log("Operation completed")
        assert "✅" in str(ctx)
