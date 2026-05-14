# gridiron_gpt/draft/fetcher.py

import requests
from typing import Dict

_FFC_URL = "https://fantasyfootballcalculator.com/api/v1/adp/{scoring}?teams={teams}&year=2025"
_ESPN_INJURIES_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries"

INJURY_PENALTIES = {
    "IR": -30.0,
    "Out": -20.0,
    "Doubtful": -10.0,
    "Questionable": -5.0,
    "Probable": -1.0,
}


def fetch_adp(scoring: str = "ppr", teams: int = 12) -> Dict[str, dict]:
    """Fetch ADP from Fantasy Football Calculator. Returns {player_name: {...}}."""
    ffc_scoring = "ppr" if scoring == "ppr" else ("half-ppr" if scoring == "half_ppr" else "standard")
    url = _FFC_URL.format(scoring=ffc_scoring, teams=teams)
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        players = resp.json().get("players", [])
        return {
            p["name"]: {
                "adp": float(p.get("adp", 9999)),
                "position": p.get("position", "UNK"),
                "team": p.get("team", "UNK"),
                "bye": p.get("bye"),
                "stdev": float(p.get("stdev", 0)),
                "times_drafted": int(p.get("times_drafted", 0)),
            }
            for p in players
            if p.get("name")
        }
    except Exception as e:
        print(f"⚠️ ADP fetch failed: {e}")
        return {}


def fetch_injuries() -> Dict[str, str]:
    """Fetch current ESPN injury reports. Returns {player_name: status_string}."""
    try:
        resp = requests.get(_ESPN_INJURIES_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        injuries = {}
        for team_entry in data.get("injuries", []):
            for inj in team_entry.get("injuries", []):
                name = inj.get("athlete", {}).get("displayName", "")
                status = inj.get("status", "")
                if name:
                    injuries[name] = status
        return injuries
    except Exception as e:
        print(f"⚠️ Injury data unavailable ({e}), continuing without it.")
        return {}
