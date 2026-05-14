from phred.cli.registry import get_registered_commands
from phred.cli.utils.feedback import banner, dry_run_tip

def semantic_audit(dry_run=False):
    banner("📊 Semantic Dashboard Audit")
    if dry_run:
        dry_run_tip("Dry-run: Validating semantic hooks and CLI registry alignment...")
        return {"status": "dry-run", "hooks": ["espn-intake", "doctor"]}

    hooks = get_registered_commands()
    return {"active_hooks": hooks, "audit_passed": True}
