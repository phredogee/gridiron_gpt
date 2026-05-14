# ~/projects/my_project/gridiron_gpt/shell/doctor.xsh 🩺

import subprocess
env = __xonsh__.env

# 📦 Check if 'phred' is importable
try:
    subprocess.run(["python", "-c", "import phred"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("📦 Registry: ✅ phred")
except subprocess.CalledProcessError:
    print("📦 Registry: ❌ phred not found")

# 🧪 Check if pytest can discover phred tests
try:
    result = subprocess.run(["pytest", "--collect-only"], capture_output=True, text=True)
    if "phred" in result.stdout:
        print("🧪 Tests:    ✅ discoverable")
    else:
        print("🧪 Tests:    ❌ not found")
except Exception as e:
    print(f"🧪 Tests:    ❌ pytest failed → {e}")
