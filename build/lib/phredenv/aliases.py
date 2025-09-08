# phredenv/aliases.py

from phredenv.loader import load_phred_loader

load_phred_loader()

def load_phred():
    try:
        from xonsh.built_ins import __xonsh__
        __xonsh__.env["PHRED_DEBUG"] = True
        print("🎩 phredenv loaded in shell context.")
        # Optionally call shell setup here
        from phredenv.loader import load_phred_loader
        load_phred_loader()
    except ImportError:
        print("⚠️ phredenv can only be loaded inside a Xonsh shell.")
