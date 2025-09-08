# retriever.py

from gridiron_gpt.core.advisor import Advisor

advisor = Advisor()

def get_top_fantasy_picks(position="RB", week=1, top_k=3):
    query = f"top {position} sleepers week {week}"
    results = advisor.query(query, top_k=top_k)
    return [
        {
            "name": r["player_name"],
            "points": r["projected_points"],
            "note": r.get("note", "")
        }
        for r in results
    ]

def get_injury_risks(top_k=5):
    query = "players with high injury risk this week"
    results = advisor.query(query, top_k=top_k)
    return [
        {
            "name": r["player_name"],
            "risk": r["injury_risk"],
            "note": r.get("note", "")
        }
        for r in results
    ]
