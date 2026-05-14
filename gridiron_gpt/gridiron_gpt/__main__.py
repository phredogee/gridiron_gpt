"""
Module entrypoint for: python -m gridiron_gpt
Runs the Click CLI defined in cli/main.py.
"""
from cli.main import main as cli_main

if __name__ == "__main__":
    cli_main()
