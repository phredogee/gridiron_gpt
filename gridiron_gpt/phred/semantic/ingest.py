# phred/semantic/ingest.py

def ingest_data(source, dry_run=False):
    with FeedbackContext("info", dry_run=dry_run) as ctx:
        ctx.log(f"📥 Ingesting from: {source}")
        try:
            payload = fetch_and_parse(source)
            ctx.log("✅ Ingestion complete")
            return payload
        except Exception as e:
            ctx.debug(f"❌ Ingestion error: {e}")
            raise
