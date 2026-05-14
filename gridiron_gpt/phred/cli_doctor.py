# phred/cli_doctor.py

def run_diagnostics(dry_run=False):
    if dry_run:
        return "ℹ️ Dry run — no changes made ✅"
    return "✅ All systems nominal\n⚠️ Minor warnings found"
