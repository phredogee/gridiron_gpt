# diagnostics/embed_players.py

import typer
from semantic_pipeline.embed_cli import embed
from phred.sports.fetchers.espn import get_player_bios
from phred.sports.fetchers.nflverse import get_player_stats
# from semantic.utils.index import add_to_index  # Uncomment if implemented

app = typer.Typer()

@app.command()
def run_embedding_pipeline(
    dry_run: bool = typer.Option(False, help="Preview combined text without embedding"),
    save_to_index: bool = typer.Option(False, help="Save embeddings to semantic index")
):
    bios = get_player_bios()
    stats = get_player_stats()

    for player_id in bios:
        bio = bios[player_id]
        stat_summary = stats.get(player_id, "")
        combined = f"{bio} {stat_summary}".strip()

        print(f"\n📌 Player: {player_id}")
        if dry_run:
            print(f"🧪 Preview:\n{combined}")
            continue

        try:
            embedding = embed(text=combined)
            print(f"✅ Embedded vector for {player_id}")

            if save_to_index:
                # add_to_index(player_id, embedding)  # Uncomment when ready
                print(f"📦 Saved to index: {player_id}")
        except Exception as e:
            print(f"⚠️ Error embedding {player_id}: {e}")

if __name__ == "__main__":
    app()
