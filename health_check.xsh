# ~/projects/my_project/health_check.xsh

from datetime import datetime
import shutil
import subprocess

if '__health_check_loaded__' not in locals():
    __health_check_loaded__ = True

    # 🩺 Timestamped health check
    print(f"🩺 Shell Health Check: {datetime.now()}")

    # 🧠 Neovim availability check
    nvim_path = shutil.which("nvim")
    if nvim_path:
        try:
            version = subprocess.run(["nvim", "--version"], capture_output=True, text=True).stdout.splitlines()[0]
            print(f"🧠 Neovim available: {version}")
        except Exception as e:
            print(f"⚠️ Neovim found but version check failed: {e}")
    else:
        print("⚠️ Neovim not found")
