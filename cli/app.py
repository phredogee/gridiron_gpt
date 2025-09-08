import typer
from cli.commands.audit_cmd import audit_cmd
from cli.commands.ingest_cmd import ingest_cmd
from cli.commands.validate_cmd import validate_cmd

app = typer.Typer()
app.add_typer(audit_cmd, name="audit")
app.add_typer(ingest_cmd, name="ingest")
app.add_typer(validate_cmd, name="validate")

def main():
    app()
