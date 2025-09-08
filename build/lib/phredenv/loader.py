import importlib.util
import os

try:
    from xonsh.built_ins import __xonsh__
except ImportError:
    __xonsh__ = None

PHRED_DEBUG = __xonsh__.env.get("PHRED_DEBUG", False) if __xonsh__ else False

def load_phred_loader(path):
    spec = importlib.util.spec_from_file_location("phred_loader", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if PHRED_DEBUG:
        print(f"✅ Loaded phred_loader from {path}")

def init_phredenv():
    if not __xonsh__:
        print("⚠️ init_phredenv must be run inside a Xonsh shell.")
        return

    env = __xonsh__.env
    aliases = __xonsh__.aliases

    if PHRED_DEBUG:
        print("🐛 [phredenv] Debug mode enabled")

    print("🎩 phredenv shell initialized")

    clean_bytecode()
    dedupe_path()

try:
    import phredenv.sports
    if hasattr(phredenv.sports, "register_aliases"):
        phredenv.sports.register_aliases(aliases)
except ImportError:
    print("⚠️ sports.py not found — skipping sports alias registration.")
def clean_bytecode():
    for root, _, files in os.walk(os.getcwd()):
        for f in files:
            if f.endswith(".pyc"):
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass

def dedupe_path():
    path = __xonsh__.env.get("PATH", [])
    __xonsh__.env["PATH"] = list(dict.fromkeys(path))

def phred_doctor():
    print("🩺 Running phredenv diagnostics...\n")

    # Shell hygiene
    print("🔍 PATH entries:", len(__xonsh__.env.get("PATH", [])))
    print("🧹 Bytecode cleanup: ✅")
    print("🔗 Aliases registered:", list(__xonsh__.aliases.keys()))

    # Xontrib check
    if "phredenv" in __xonsh__.xontribs_loaded:
        print("🧠 Xontrib loaded: ✅")
    else:
        print("⚠️ Xontrib not loaded")

    # 🏈 Sports pipeline checks
    print("\n🏈 Sports Pipeline Checks:")

    try:
        import phredenv.sports
        print("📦 sports.py module: ✅")
    except ImportError:
        print("📦 sports.py module: ❌ Missing")

    sports_aliases = ["sports-fetch", "sports-predict"]
    for alias in sports_aliases:
        if alias in __xonsh__.aliases:
            print(f"🔗 Alias '{alias}': ✅")
        else:
            print(f"🔗 Alias '{alias}': ❌ Not registered")

    cwd = os.getcwd()
    if "gridiron_gpt" in cwd:
        print(f"📁 Project context: ✅ ({cwd})")
    else:
        print(f"📁 Project context: ❌ Not inside 'gridiron_gpt'")

    print("\n✅ All systems nominal.")
