# phred/cli/initify.py

import os
from phred.cli.utils.feedback import banner, success

def ensure_init_files(root="phred"):
    banner(f"🧼 Ensuring __init__.py files under '{root}/'")
    created = []
    for dirpath, dirnames, _ in os.walk(root):
        for dirname in dirnames:
            init_path = os.path.join(dirpath, dirname, "__init__.py")
            if not os.path.exists(init_path):
                open(init_path, "a").close()
                created.append(init_path)
    if created:
        for path in created:
            success(f"Created: {path}")
    else:
        success("All __init__.py files already in place.")

if __name__ == "__main__":
    ensure_init_files()
