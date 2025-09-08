# ~/phredenv/phred_loader.py

    # Color segments
    cwd_colored = f"\033[1;34m{cwd}\033[0m"
    user_colored = f"\033[1;32m{user}\033[0m"
    branch_colored = f"\033[1;33m{branch}\033[0m" if branch else ""

    prefix = f"{project}/" if project and project != cwd else ""

    return f"{prefix}{cwd_colored} 🧠 {user_colored} {branch_colored} > "

# 🔄 Register dynamic prompt hook
@events.on("preprompt")
def _phred_prompt():
    __xonsh__.env["PROMPT"] = build_prompt()
    if PHRED_DEBUG:
        print(f"🎨 Prompt updated to: {__xonsh__.env['PROMPT']}")

import importlib.util
import os

project_root = os.path.dirname(__xonsh__.env['PWD'])
loader_path = os.path.join(project_root, "phredenv", "phred_loader.py")

def load_phred_loader(path):
    spec = importlib.util.spec_from_file_location("phred_loader", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if __xonsh__.env.get("PHRED_DEBUG", False):
        print(f"✅ Loaded phred_loader from {path}")

if os.path.isfile(primary_path):
    load_phred_loader(primary_path)
elif os.path.isfile(fallback_path):
    load_phred_loader(fallback_path)
else:
    print("⚠️ phred_loader.py not found in either location.")

def load_phred(args=None):
    import importlib.util, os

    paths = [
        os.path.expanduser("~/gridiron_gpt/phredenv/phred_loader.py"),
        os.path.expanduser("~/projects/my_project/phredenv/phred_loader.py")
    ]

    for path in paths:
        if os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("phred_loader", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            print(f"✅ Loaded phred_loader from {path}")
            return

    print("❌ phred_loader.py not found in any known location.")


aliases['load-phred'] = load_phred
