# profile_validator.py

from semantic.utils.feedback import error, success, onboarding_tip

SUPPORTED_SOURCES = {"espn", "nflverse", "fantasypros"}

def validate_profile(source: str, dry_run: bool = True):
    if source not in SUPPORTED_SOURCES:
        error(f"Unsupported source: '{source}'")
        onboarding_tip(f"Try one of: {', '.join(SUPPORTED_SOURCES)}")
        raise ValueError(f"Invalid source: {source}")

    if dry_run:
        onboarding_tip("Dry-run mode — no changes will be committed.")

    success(f"Profile validated for source: {source}")
