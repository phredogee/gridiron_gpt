#!/bin/bash

# Define the code to prepend
PREPEND_CODE='source ~/projects/my_project/gridiron_gpt/emoji_palette.xsh
banner_icon = get_seasonal_icon("autumn")'

# Loop through all .xsh files in the target directory

for file in ~/projects/my_project/gridiron_gpt/*.xsh; do
    grep -q "emoji_palette.xsh" "$file" || sed -i '1i\
source ~/projects/my_project/gridiron_gpt/emoji_palette.xsh\nbanner_icon = get_seasonal_icon("autumn")
' "$file"
done

    # Prepend the code safely
    tmpfile=$(mktemp)
    echo "$PREPEND_CODE" > "$tmpfile"
    cat "$file" >> "$tmpfile"
    mv "$tmpfile" "$file"
    echo "✅ Prepended emoji banner logic to $file"
done
