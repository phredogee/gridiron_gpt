# phred/semantic/transform.py

def transform_payload(payload, dry_run=False):
    with FeedbackContext("info", dry_run=dry_run) as ctx:
        ctx.log("🔧 Transforming payload")
        try:
            transformed = apply_rules(payload)
            ctx.log("✅ Transformation successful")
            return transformed
        except Exception as e:
            ctx.debug(f"❌ Transformation failed: {e}")
            raise
