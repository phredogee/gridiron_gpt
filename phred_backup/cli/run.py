from phred.cli.registry import run_command, list_commands
import sys

def cli_main():
    if len(sys.argv) < 2:
        print("❌ No command provided.")
        print("📜 Available commands:", ", ".join(list_commands()))
        sys.exit(1)

    cmd = sys.argv[1]
    try:
        run_command(cmd)
    except Exception as e:
        print(f"❌ Error running '{cmd}':", e)
        sys.exit(1)
