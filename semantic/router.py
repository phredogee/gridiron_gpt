# semantic/router.py

import json
import os
from semantic.profile_delta import compute_profile_delta

# from semantic.parser import nlp
from semantic.utils.feedback import banner, success, warning, error

# 🧠 NLP-powered query router: interprets player queries like "rushing yards for Bijan"

def route_query(text: str, dry_run=False):
    from gridiron_gpt.cli.rushing import run_rushing_query
    from gridiron_gpt.cli.receiving import run_receiving_query

    doc = nlp(text)
    banner(f"🧠 Interpreting query: '{text}'")

    entities = {ent.label_: ent.text for ent in doc.ents}
    for label, value in entities.items():
        print(f"🔍 {label}: {value}")

    player = entities.get("PERSON")

    query_map = {
        "rushing": run_rushing_query,
        "receiving": run_receiving_query,
        # Future: "targets": run_target_query
    }

    matched = False
    for keyword, func in query_map.items():
        if keyword in text.lower():
            print(f"📊 Stat: {keyword.title()} Yards")
            matched = True
            if player:
                print(f"🏈 Player: {player}")
                if not dry_run:
                    func(player=player)
            else:
                warning("⚠️ No player found in query")
            break

    if not matched:
        error("🤷 Query type not recognized")

def route_prompt(prompt: str) -> str:
    if "injury" in prompt.lower():
        return "injury_module"
    elif "trade" in prompt.lower():
        return "trade_analyzer"
    else:
        return "general_gpt"

# 🔁 Semantic ingestion router
def route_semantic_ingestion(source: str, identifier: int, profile: str = None):
    from semantic.profile_delta import compute_profile_delta
    from semantic.matchup_diff import compute_matchup_diff
    from semantic.roster_embed import generate_roster_embedding

    path_map = {
        "espn": f"data/clean/espn/week_{identifier}.json",
        "nflverse": f"data/clean/nflverse/season_{identifier}.json"
    }

    path = path_map.get(source)
    if not path:
        fail_banner(f"🚫 Unsupported source: {source}")
        return

    if not os.path.exists(path):
        fail_banner(f"📁 No cleaned data found at {path}")
        return

    banner(f"🧠 Routing {source.upper()} data to semantic modules...")

    try:
        with open(path, "r") as f:
            data = json.load(f)
    except Exception as e:
        fail_banner(f"❌ Failed to load data: {str(e)}")
        return

    if profile:
        delta = compute_profile_delta(data, profile)
        success_banner(f"✅ Profile delta computed for {profile}")
        return delta

def route_matchups(source: str, season: int, league_id: str):
    banner(f"📦 Routing matchups from {source.upper()} for season {season}")

    # Placeholder: Load ingested data (replace with actual ESPN ingestion output)
    raw_data = load_ingested_data(source, season, league_id)

    matchups = []
    for entry in raw_data:
        matchups.append({
            "team_a": entry["home_team"],
            "team_b": entry["away_team"],
            "score_a": entry.get("home_score", 0),
            "score_b": entry.get("away_score", 0),
            "week": entry["week"]
        })

    return matchups

def load_ingested_data(source, season, league_id):
    # Stub: Replace with actual ESPN ingestion output path or object
    return [
        {"home_team": "Falcons", "away_team": "Panthers", "home_score": 24, "away_score": 17, "week": 1},
        {"home_team": "Bills", "away_team": "Jets", "home_score": 21, "away_score": 27, "week": 1}
    ]

    # Future: embed roster or run matchup diff
    # generate_roster_embedding(data)
    # compute_matchup_diff(data, team_a, team_b)
