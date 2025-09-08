# gridiron_gpt/cli/main.py

import click
from .espn import espn  # assuming espn.py defines a click group called espn

@click.group()
def cli():
    """Main CLI entry point"""
    pass

cli.add_command(espn)
