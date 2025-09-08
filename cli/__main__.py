# gpt/cli/__main__.py

import argparse
from gpt.cli.doctor import run_diagnostics

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

run_diagnostics(dry_run=args.dry_run)
