# phred/semantic/validate.py

from phred.feedback.context import FeedbackContext

def validate_schema(data, schema, dry_run=False):
    with FeedbackContext("warn", dry_run=dry_run) as ctx:
        ctx.log("🔎 Validating schema")
        for field in schema:
            if field not in data:
                ctx.debug(f"⚠️ Missing field: {field}")
        ctx.log("✅ Validation complete")
        return ctx.render()
