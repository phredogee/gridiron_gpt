# tests/test_feedback_context.py

from phred.utils.banner_utils import feedback_context

def test_emit_success_message(capsys):
    ctx = feedback_context("Operation succeeded", level="success")
    with ctx:
        pass
    output = capsys.readouterr().out
    assert "✅ Operation succeeded" in output

def test_dry_run_logging():
    ctx = feedback_context("Dry run test", level="debug", dry_run=True)
    with ctx:
        ctx.debug("This is a debug message")
    assert "DRY-RUN DEBUG: This is a debug message" in ctx.logs
