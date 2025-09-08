# semantic/dashboard.py

from semantic.utils.feedback import banner

def summarize_matchups(matchups: list):
    banner("📊 Summarizing matchups for dashboard insights")

    summaries = []
    for m in matchups:
        winner = m["team_a"] if m["score_a"] > m["score_b"] else m["team_b"]
        summaries.append({
            "week": m["week"],
            "matchup": f"{m['team_a']} vs {m['team_b']}",
            "score": f"{m['score_a']}–{m['score_b']}",
            "winner": winner
        })

    return {
        "total_matchups": len(matchups),
        "summaries": summaries
    }
