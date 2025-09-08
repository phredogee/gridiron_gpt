def get_player_stats(pos=None, team=None, metric=None, range=None):
    # Build ESPN API URL and params
    url = f"https://api.espn.com/stats"
    params = {
        "position": pos,
        "team": team,
        "stat": metric,
        "timeframe": range,
    }
    response = requests.get(url, params=params)
    return response.json()
