# utils/cli_base.py

from utils.banner_utils import (
    print_banner,
    print_section,
    print_success,
    print_warning,
    print_error,
    print_dry_run,
)

def init_cli(title: str, emoji: str = "🚀", dry_run: bool = False) -> None:
    print_banner(title, emoji)
    if dry_run:
        print_dry_run("Dry-run mode enabled. No changes will be made.")

def guard_status(name: str, status: bool) -> None:
    emoji = "🟢" if status else "🔴"
    print(f"{emoji} Guard: {name} = {status}")
