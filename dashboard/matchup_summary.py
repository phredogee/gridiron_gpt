# dashbaord/matchup_summary.py

from semantic.profile_delta import load_team_profile, compare_profiles
from utils.banner_utils import banner, success_banner

def generate_summary(team_a, team_b, source, identifier, profile):
    banner(f"📝 Generating summary for {team_a} vs {team_b} — {source.upper()} {identifier} [{profile}]")

    profile_a = load_team_profile(team=team_a, source=source, identifier=identifier, profile=profile)
    profile_b = load_team_profile(team=team_b, source=source, identifier=identifier, profile=profile)

    diff = compare_profiles(profile_a, profile_b)

    summary_lines = []

    for metric, delta in diff.items():
        if delta > 0:
            summary_lines.append(f"🔺 {team_a} leads in {metric} by {delta:.2f}")
        elif delta < 0:
            summary_lines.append(f"🔻 {team_b} leads in {metric} by {abs(delta):.2f}")
        else:
            summary_lines.append(f"⚖️ {metric} is evenly matched")

    success_banner("✅ Summary generated")
    return "\n".join(summary_lines)
