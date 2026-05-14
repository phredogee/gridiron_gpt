# gridiron_gpt/cli/main.py

'''
┌────────────────────────────────────────────┐
│  CLI Entrypoint Export Map                 │
├────────────┬───────────────────────────────┤
│ cli()      │ Click group for commands      │
│ main()     │ Entrypoint for CLI execution  │
│ __all__    │ Explicit exports for __init__ │
└────────────┴───────────────────────────────┘
'''


import click
from .espn import espn
from .ask import ask
from .draft import draft

@click.group()
def cli():
    """🏈 GridironGPT — fantasy football analytics CLI"""
    pass

cli.add_command(espn)
cli.add_command(ask)
cli.add_command(draft)

__all__ = ["cli", "main"]

def main():
    cli()
