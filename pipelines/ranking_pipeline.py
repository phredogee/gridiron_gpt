# pipelines/ranking_pipeline.py

from phred.sports.fetch import fetch_from_espn
from phred.utils.banner_utils import banner

def run_pipeline_logic(season: int = 2024, dry_run: bool = True) -> dict:
    banner(f"Running ranking pipeline for season {season} (dry_run={dry_run})", kind="info")

    # Step 1: Fetch raw ESPN data
    data = fetch_from_espn(season=season, dry_run=dry_run)
    players = data.get("players", [])

    # Step 2: Apply ranking logic (stubbed for now)
    ranked_players = sorted(players, key=lambda p: p.get("score", 0), reverse=True)

    # Step 3: Return structured output
    result = {
        "season": season,
        "count": len(ranked_players),
        "rankings": ranked_players
    }

    banner(f"Pipeline completed with {len(ranked_players)} players", kind="success")
    return result

if __name__ == "__main__":
    output = run_pipeline_logic(season=2024, dry_run=True)
    print(output)
