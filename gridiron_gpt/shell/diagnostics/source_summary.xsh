# ─────────────────────────────────────────────────────────────
# 📦 source_summary.xsh — Contributor Sourcing Summary
# ─────────────────────────────────────────────────────────────

print("📦 Modules sourced this session:")
print("├── doctor.xsh")
print("├── pipeline_diagnostics.xsh")
print("├── matchup_diagnostics.xsh")
print("├── emoji_palette/diagnostics_fall.xsh")
print("└── helpers/source_utils.xsh")

# Optional: Rotate seasonal affirmations
from datetime import datetime
now = datetime.now()
month = now.month
day = now.day

if month == 10 and day >= 15:
    print("🎃 Spooky good diagnostics incoming!")
elif month in [9, 10, 11]:
    print("🍂 Cozy contributors make the best calls.")
elif month in [12, 1, 2]:
    print("❄️ Your shell is proud of you.")
elif month in [3, 4, 5]:
    print("🌸 Every sourced module is a teaching moment.")
else:
    print("🌞 Contributors make sunny progress!")

# Optional: Log sourcing time if available
if 'SOURCE_START' in env and 'SOURCE_END' in env:
    duration = env['SOURCE_END'] - env['SOURCE_START']
    print(f"⏱️ Sourcing completed in {duration:.2f} seconds.")

source helpers/visuals/emoji_rotation.xsh
$emoji = $(pick_rotating_emoji)
print(f"{emoji} Sourcing summary complete. Your shell is proud of you.")

if 'EMOJI_THEME' in env:
    theme = env['EMOJI_THEME'].lower()
    if theme == 'halloween':
        print("🎃 Haunted sourcing complete. Diagnostics are alive!")
    elif theme == 'cozy':
        print("🫖 Cozy contributors make the best calls.")
