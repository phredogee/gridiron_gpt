# phred/cli/espn.py

from phred.sports.espn import fetch_from_espn
from phred.feedback import banner

def fetch_espn_data(season, limit=None, dry_run=False):
    """
    CLI entrypoint to fetch ESPN data.
    """
    season = int(season)

    if dry_run:
        # Predictable dry-run payload for tests
        players = [
            {
                "playerId": f"P{i+1:03}",
                "name": f"Test Player {i+1}",
                "team": "Testers",
                "position": "QB",
                "score": 100 - i
            }
            for i in range(10)
        ]
        if limit is not None:
            players = players[:limit]
        return {
            "season": season,
            "players": players,
            "count": len(players),
            "dry_run": True
        }

    # Live mode: call the real fetcher
    data = fetch_from_espn(season=season, dry_run=False)

    if limit is not None and "players" in data:
        data["players"] = data["players"][:limit]
        data["count"] = len(data["players"])

    data["dry_run"] = dry_run
    banner(f"Fetched {data.get('count', 0)} players for season {season}", level="success")
    return data

def fetch_from_espn(season=None, dry_run=False):
    """
    Minimal stub for ESPN fetcher so tests can run without hitting the network.
    Returns predictable fake data in dry-run mode.
    """
    if dry_run:
        players = [
            {
                "playerId": f"P{i+1:03}",
                "name": f"Test Player {i+1}",
                "team": "Testers",
                "position": "QB",
                "score": 100 - i
            }
            for i in range(10)
        ]
        return {
            "season": season,
            "players": players,
            "count": len(players),
            "dry_run": True
        }

    # TODO: Implement real ESPN fetch logic here
    raise NotImplementedError("Live ESPN fetch not implemented yet.")
