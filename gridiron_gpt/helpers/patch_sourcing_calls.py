#!/usr/bin/env python3
import os
import re

print("🔧 Patching source @file calls across your shell ecosystem...")

paths = [
    os.path.expanduser("~/.xonshrc.d"),
    os.path.expanduser("~/.config/xonsh"),
    os.path.expanduser("~/.xonshrc"),
]

for root in paths:
    if not os.path.exists(root):
        continue

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if not fname.endswith(".xsh"):
                continue

            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r") as f:
                lines = f.readlines()

            patched = []
            changed = False
            for line in lines:
                match = re.search(r"source\s+@(\w[\w\d_\.\/-]*)", line)
                if match:
                    var = match.group(1)
                    changed = True
                    patched.append(f"if {var} and os.path.isfile({var}):\n")
                    patched.append(f"    try:\n")
                    patched.append(f"        source @{var}\n")
                    patched.append(f"        print(f\"🧩 Sourced: {{{var}}}\")\n")
                    patched.append(f"    except Exception as e:\n")
                    patched.append(f"        print(f\"⚠️ Failed to source {{{var}}}: {{e}}\")\n")
                    patched.append(f"else:\n")
                    patched.append(f"    print(f\"⚠️ Skipped invalid file: {{{var}}}\")\n")
                else:
                    patched.append(line)

            if changed:
                backup = fpath + ".bak"
                os.rename(fpath, backup)
                with open(fpath, "w") as f:
                    f.writelines(patched)
                print(f"🛠️ Patched: {fpath} (backup saved as {backup})")

print("✅ All source calls patched safely.")
