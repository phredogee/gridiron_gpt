# phred/feedback/core.py

def generate_feedback(dry_run=False, return_logs=False):
    logs = []
    if dry_run:
        logs.append("ℹ️ Dry run — no changes made")
    logs.append("✅ All systems nominal")
    logs.append("⚠️ Minor warnings found")
    logs.append("❌ Critical issue detected")

    return logs if return_logs else "\n".join(logs)
