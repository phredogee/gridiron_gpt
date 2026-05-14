# /gridiron_gpt/semantic/query_dispatcher.py

def dispatch_player_query(player: str, week: int):
    raw = fetch_player_data(player_name=player, week=week)
    clean = preprocess_players([raw])
    return clean[0]
