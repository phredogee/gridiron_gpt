# gridiron_gpt/openai_wrapper.py

from importlib import import_module
from importlib.metadata import version, PackageNotFoundError

def run_openai_diagnostics():
    try:
        v = version("openai")
        print(f"📦 OpenAI SDK version: {v}")
    except PackageNotFoundError:
        print("🚫 OpenAI SDK not found")

    try:
        import_module("openai")
        print("✅ SDK import succeeded")
    except Exception as e:
        print(f"⚠️ Import error: {e}")

    print("🎯 OpenAI diagnostics complete.\n")
