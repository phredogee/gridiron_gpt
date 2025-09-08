def run_predict(args):
    print(f"Predicting for {args.position} in {args.weather}")
    if args.verbose:
        print("Verbose mode enabled")
    if args.slack:
        print("Sending prediction to Slack...")

def register(subparsers):
    parser = subparsers.add_parser("predict", help="Run prediction")
    parser.add_argument("--position", required=True)
    parser.add_argument("--weather", required=True)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--slack", action="store_true")
    parser.set_defaults(func=run_predict)
