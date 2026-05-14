# gpt/modules/semantic_router.py

import typer
import re
from gridiron_gpt.modules.fetch_raw_data import fetch_player_data
from gridiron_gpt.modules.preprocess_data import preprocess_players
from gridiron_gpt.utils.banner import print_banner

app = typer.Typer()

@app.command()
def route(query: str, dry_run: bool = False):
    # 🧠 Regex parsing block
    match = re.match(r"(.*)\s+player=(\w+)\s+week=(\d+)", query)
    if not match:
        print_banner("❌ Invalid query format. Use: '<semantic_query> player=<name> week=<number>'", level="error")
        raise typer.Exit(code=1)

    semantic_query, player, week = match.groups()
    week = int(week)

    # ✅ Expressive feedback
    print_banner(f"🔍 Routing semantic query: '{semantic_query}'")
    print_banner(f"🏈 Player: {player} | 📅 Week: {week}")

    if dry_run:
        print_banner("🧪 Dry-run mode: previewing fetch and preprocess steps", level="info")
        print_banner(f"📦 Would fetch data for {player}, week {week}", level="warn")
        return

    try:
        raw = fetch_player_data(player_name=player, week=week)
        clean = preprocess_players([raw])
        stats = clean[0]

        print_banner(f"🏈 {stats['name']} in Week {week}:", level="info")
        print_banner(f"• Position: {stats['position']}", level="info")
        print_banner(f"• Total Yards: {stats['yards']}", level="info")
        print_banner(f"• Touchdowns: {stats['touchdowns']}", level="info")

    except Exception as e:
        print_banner(f"❌ Routing failed: {str(e)}", level="error")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
