#!/bin/bash
# 🧩 GridIron GPT — Patch sourcing calls to prevent RuntimeError

echo "🔧 Patching source @file calls across your shell ecosystem..."

find ~/.xonshrc.d ~/.config/xonsh ~/.xonshrc -type f -name "*.xsh" | while read -r file; do
    if grep -q 'source @' "$file"; then
        echo "🛠️ Patching: $file"

        # Backup original
        cp "$file" "$file.bak"

        # Replace raw source calls with guarded try/except blocks
        sed -i '/source @/{
            s/source @\(.*\)/if \1 and os.path.isfile(\1):\\
    try:\\
        source @\1\\
        print(f"🧩 Sourced: {\1}")\\
    except Exception as e:\\
        print(f"⚠️ Failed to source {\1}: {e}")\\
else:\\
    print(f"⚠️ Skipped invalid file: {\1}")/
        }' "$file"
    fi
done

echo "✅ All source calls patched. Backups saved as *.bak"
