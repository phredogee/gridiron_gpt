# phred/feedback/core.py

def generate_feedback(dry_run=False, return_logs=False):
    logs = []
    if dry_run:
        logs.append("ℹ️ Dry run — no changes made")
    logs.append("✅ Operation completed")
    return logs if return_logs else "\n".join(logs)
