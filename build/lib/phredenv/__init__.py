# phredenv/__init__.py

from .env import setup_env
from .banner import show_banner
from phredenv.loader import init_phredenv

def is_xonsh_shell():
    """Safe check for Xonsh context."""
    try:
        import builtins
        return hasattr(builtins, '__xonsh__')
    except ImportError:
        return False

def load(debug=False):
    if debug:
        print("🐛 [phredenv] Debug mode enabled")

    if is_xonsh_shell():
        show_banner()  # Optional: only show banner in shell context

    try:
        init_phredenv()
        print("🎩 phredenv loaded successfully.")
    except Exception as e:
        print(f"❌ [phredenv] Failed to initialize: {e}")

__xontrib__ = {
    "load": load
}
