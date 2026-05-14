# phred/semantic/query_engine.py

from phred.feedback.context import FeedbackContext

def run_query(query: str, dry_run=False):
    with FeedbackContext("info", dry_run=dry_run) as ctx:
        ctx.log(f"🔍 Executing query: {query}")
        try:
            result = execute_query(query)
            ctx.log("✅ Query executed successfully")
            return result
        except Exception as e:
            ctx.debug(f"❌ Query failed: {e}")
            raise
