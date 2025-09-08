"""
🧭 Walkthrough: Environment Activation & Shell Quirks

This module helps contributors understand:
- How activation routines behave across shells
- How to detect and fix shell mismatches
- How to validate environment state with expressive feedback
"""

import os
import pytest
import subprocess

def test_virtualenv_active():
    """Check if the virtual environment is active."""
    venv = os.environ.get("VIRTUAL_ENV")
    assert venv is not None, "❌ Virtual environment not active"
    print(f"✅ Virtual environment detected: {venv}")

def test_python_path_consistency():
    """Ensure Python path matches expected virtualenv."""
    result = subprocess.run(["which", "python"], capture_output=True, text=True)
    python_path = result.stdout.strip()
    assert "phredenv" in python_path, f"❌ Unexpected Python path: {python_path}"
    print(f"✅ Python path is correct: {python_path}")

@pytest.mark.skipif(os.environ.get("SHELL", "").endswith("xonsh"), reason="Xonsh shell detected")
def test_shell_specific_behavior():
    """Skip this test if running in Xonsh — shell-specific logic goes elsewhere."""
    print("✅ Non-Xonsh shell detected, running shell-specific test")

def test_xonsh_activation_hint():
    """Provide guidance if Xonsh shell is detected."""
    shell = os.environ.get("SHELL", "")
    if shell.endswith("xonsh"):
        print("⚠️ Xonsh shell detected — ensure you run `source activate.xsh` or use `xontrib` if needed")
    else:
        print("✅ Shell is not Xonsh — standard activation applies")
