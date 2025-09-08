# scripts/doctor.py

from phred.utils.banner_utils import feedback_context

def run_diagnostics():
    with feedback_context("Checking environment setup...", level="info") as ctx:
        import sys
        ctx.debug(f"Python executable: {sys.executable}")
        ctx.debug(f"PYTHONPATH: {sys.path}")

        try:
            from phred.cli.utils import feedback
            ctx.emit("✅ CLI feedback module is importable")
        except ImportError:
            ctx.fail("❌ CLI feedback module not found")

if __name__ == "__main__":
    run_diagnostics()
