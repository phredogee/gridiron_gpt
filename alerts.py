from core.slack_bot import SlackBot
from core.advisor import Advisor

bot = SlackBot("https://hooks.slack.com/services/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")
advisor = Advisor()

def send_player_alert(players, confidence):
    message = "*GridironGPT Alert:*\n"
    for player in players:
        message += f"• _{player['name']}_ {player.get('note', '')} – Projected {player['points']} pts\n"
    message += f":chart_with_upwards_trend: Confidence: {confidence}"
    bot.send_message(message)

def get_top_fantasy_picks():
    # Replace with actual retrieval logic
    return [
        {"name": "Ty Chandler", "points": 12.4, "note": "vs TB"},
        {"name": "Roschon Johnson", "points": 9.1, "note": "– High upside sleeper"}
    ]

def calculate_confidence(picks):
    return round(sum(p["points"] for p in picks) / (len(picks) * 15), 2)
