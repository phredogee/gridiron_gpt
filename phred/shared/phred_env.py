from phred_paths import dedupe_path

# Set session flags
__xonsh__.env["PHRED_SESSION_ACTIVE"] = True
__xonsh__.env["PHRED_DEBUG"] = True  # or False, or pulled from a config file

# Clean up PATH
dedupe_path(verbose=True)
