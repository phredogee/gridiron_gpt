from semantic.utils.feedback import banner
from profile_validator import validate_profile
from semantic.audit import audit_espn

@audit_cmd.command()
def run(source: str = "espn", dry_run: bool = True):
    banner("🧠 Semantic audit module initialized")
    validate_profile(source=source, dry_run=dry_run)
    audit_espn(source=source, dry_run=dry_run)
