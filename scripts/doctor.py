# scripts/doctor.py

from phred.feedback import FeedbackContext

def run_diagnostics():
    with FeedbackContext("Checking environment setup...", level="info") as ctx:
        import sys
        ctx.debug(f"Python executable: {sys.executable}")
        ctx.debug(f"PYTHONPATH: {sys.path}")

        try:
            from phred.cli.utils import feedback
            ctx.log("✅ CLI feedback module is importable")
        except ImportError:
            ctx.log("❌ CLI feedback module not found")

if __name__ == "__main__":
    run_diagnostics()
