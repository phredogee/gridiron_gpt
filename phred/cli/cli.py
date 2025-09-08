# gridiron_gpt/cli.py

import typer
from cli.commands import espn_cmd
from cli_modules.doctor import doctor_app  # 👈 new import

app = typer.Typer()
app.add_typer(espn_cmd.app, name="espn")
app.add_typer(doctor_app, name="doctor")   # 👈 new command group

if __name__ == "__main__":
    app()
