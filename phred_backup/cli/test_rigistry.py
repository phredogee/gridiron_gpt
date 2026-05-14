# /gpt/phred/cli/command_registry.py

import typer
from phred.cli.commands import ingest, doctor, dashboard  # example modules

app = typer.Typer()

app.command()(ingest.run)
app.command()(doctor.check)
app.command()(dashboard.launch)

def setup_commands():
    return app
