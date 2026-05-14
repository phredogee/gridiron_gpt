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
from .espn import espn  # assuming espn.py defines a click group called espn

@click.group()
def cli():
    """Main CLI entry point"""
    pass
cli.add_command(espn)

__all__ = ["cli", "main"]

def main():
    cli()
