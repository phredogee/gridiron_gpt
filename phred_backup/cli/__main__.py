from phred.cli.registry import expose_cli
from phred.cli.utils.feedback import banner

def main():
    banner("🚀 Welcome to Phred CLI")
    expose_cli()  # Dynamically exposes all @register_command functions

if __name__ == "__main__":
    main()
