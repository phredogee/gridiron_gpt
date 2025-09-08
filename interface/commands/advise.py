def run_advise(args):
    print(f"Running semantic query: {args.query}")

def register(subparsers):
    parser = subparsers.add_parser("advise", help="Run semantic query")
    parser.add_argument("--query", required=True)
    parser.set_defaults(func=run_advise)
