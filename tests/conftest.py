
import pytest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print("🧠 Injected project root into sys.path for test discovery.")

@pytest.fixture
def is_xonsh():
    return os.environ.get("SHELL", "").endswith("xonsh")

@pytest.fixture
def virtualenv_path():
    return os.environ.get("VIRTUAL_ENV", "")

def pytest_terminal_summary(terminalreporter, exitstatus):
    if exitstatus == 0:
        terminalreporter.write("🎉 All tests passed!\n")
    else:
        terminalreporter.write("💥 Some tests failed. Check logs above.\n")

