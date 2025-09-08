# gpt/cli/doctor.py

from phred.feedback import feedback_context, banner
from semantic.dashboard import hooks

def run_diagnostics(dry_run=False):
    with feedback_context("Validating semantic hooks", level="info", dry_run=dry_run):
        if not hooks.registry_exposed():
            print(banner("Registry not exposed", status="error"))
        else:
            print(banner("Registry exposed successfully", status="success"))

    with feedback_context("Checking onboarding modules", level="info", dry_run=dry_run):
        missing = hooks.check_missing_modules()
        if missing:
            for mod in missing:
                print(banner(f"Missing module: {mod}", status="warning"))
        else:
            print(banner("All onboarding modules present", status="success"))

    with feedback_context("Verifying test hygiene", level="info", dry_run=dry_run):
        if not hooks.validate_test_discovery():
            print(banner("Test discovery failed", status="error"))
        else:
            print(banner("Test discovery passed", status="success"))
