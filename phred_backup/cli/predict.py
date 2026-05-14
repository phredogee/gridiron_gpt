from phred.cli.registry import register_command
from phred.sports.predict import run_predictions

def predict_main():
    print("🔮 Running predictions...")
    run_predictions()

register_command("predict", predict_main)
