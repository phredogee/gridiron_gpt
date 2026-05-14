# gridiron_gpt/cli/ask.py

import click
from gridiron_gpt.core.advisor import Advisor
from gridiron_gpt.feedback import banner, error


@click.command()
@click.argument("query")
@click.option("--top", default=5, show_default=True, type=int, help="Number of results to return")
def ask(query, top):
    """Ask a fantasy football question against the player index.

    Examples:\n
      python -m gridiron_gpt ask "best RB to start this week"\n
      python -m gridiron_gpt ask "top wide receivers" --top 10\n
      python -m gridiron_gpt ask "Atlanta Falcons players"
    """
    advisor = Advisor()
    try:
        advisor.load()
    except FileNotFoundError as e:
        error(str(e))
        return

    try:
        results = advisor.query(query, top_k=top)
    except RuntimeError as e:
        error(str(e))
        return

    if not results:
        banner("No results found for that query.", emoji="❓")
        return

    click.echo(f"\n🔍  {query}\n")
    click.echo(f"  {'#':<4} {'Player / Position / Team / Week / Points':<55} {'Match':>6}")
    click.echo("  " + "─" * 67)
    for i, r in enumerate(results, 1):
        pct = int(r["similarity"] * 100)
        click.echo(f"  {i:<4} {r['text']:<55} {pct:>5}%")
    click.echo()
