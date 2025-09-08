# cli/main.py
import typer
from phred.cli.doctor import doctor_app
from semantic.router import route_query

app = typer.Typer()
app.add_typer(doctor_app, name="doctor")

@app.callback()
def main():
    print("🏈 Welcome to Gridiron CLI — your semantic sports assistant\n")

@app.command()
def version():
    print("📦 Gridiron CLI version 0.3.1")

def query(text: str, dry_run: bool = False):
    """
    Run a semantic query against ESPN data.
    """
    result = route_query(text, dry_run=dry_run)
    print(result)

if __name__ == "__main__":
    app()

