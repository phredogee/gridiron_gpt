# cli/audit.py

def audit_espn_pipeline():
    banner_info("🧪 Dry-run: ESPN pipeline check")
    players = fetch_espn_players()
    if players:
        banner_info(f"✅ ESPN pipeline active: {len(players)} players ingested.")
    else:
        banner_warn("🚫 ESPN pipeline inactive or failed.")
