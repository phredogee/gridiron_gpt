# phred/cli/query.py

from phred.feedback.context import FeedbackContext
from phred.semantic.query_engine import run_query

def cli_run_query(query: str, dry_run=False):
    with FeedbackContext("info", dry_run=dry_run) as ctx:
        ctx.log(f"🧠 CLI received query: {query}")
        try:
            result = run_query(query, dry_run=dry_run)
            ctx.log("✅ Query completed")
            print(ctx.render())
            return result
        except Exception as e:
            ctx.debug(f"❌ CLI query failed: {e}")
            print(ctx.render())
            raise
