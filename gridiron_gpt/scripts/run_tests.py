# scripts/run_tests.py
import subprocess

def run():
    print("🧪 Running test suite...")
    subprocess.run(["pytest", "tests/", "--maxfail=10", "-v"])
    print("🌈 Test run complete.")

if __name__ == "__main__":
    run()
