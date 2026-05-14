# phred/sports/fetchers/espn/bios.py

from .fetch import fetch_from_espn

def get_player_bios(players, dry_run=False):
    """
    Extracts player bios from ESPN data.

    Args:
        players (list): List of player dictionaries.
        dry_run (bool): If True, adds dry-run metadata to each bio.

    Returns:
        list: List of player bios.
    """
    bios_data = []
    for player in players:
        bios_data.append({
            "name": player.get("name", "Unknown"),
            "team": player.get("team", "Unknown"),
            "position": player.get("position", "N/A"),
            "dry_run": dry_run
        })
    return bios_data

# 🧪 Dry-run stub for testing
if __name__ == "__main__":
    data = fetch_from_espn(season=2024, dry_run=True)
    bios = get_player_bios(data.get("players", []), dry_run=True)
    print("🧪 Dry-run bios preview:")
    for bio in bios:
        print(f"🔹 {bio['name']} ({bio['team']}) — {bio['position']}")
