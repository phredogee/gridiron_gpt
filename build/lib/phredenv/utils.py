# phredenv/utils.py

from xonsh.tools import is_xonsh_shell

def xonsh_only(fn):
    def wrapper(*args, **kwargs):
        if is_xonsh_shell():
            return fn(*args, **kwargs)
        else:
            print(f"⚠️ {fn.__name__} skipped — not in Xonsh shell.")
    return wrapper
