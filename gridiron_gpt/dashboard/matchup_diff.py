

from semantic.profile_delta import load_team_profile, compare_profiles
from utils.banner_utils import banner, success_banner, fail_banner

def run_matchup_diff(team_a: str, team_b: str, source: str, identifier: int, profile: str):
    banner(f"🔍 Comparing {team_a} vs {team_b} — {source.upper()} {identifier} [{profile}]")

    try:
        profile_a = load_team_profile(team=team_a, source=source, identifier=identifier, profile=profile)
        profile_b = load_team_profile(team=team_b, source=source, identifier=identifier, profile=profile)

        diff = compare_profiles(profile_a, profile_b)
        success_banner("✅ Matchup diff generated")
        return diff
    except Exception as e:
        fail_banner(f"❌ Matchup diff failed: {str(e)}")
        return None
