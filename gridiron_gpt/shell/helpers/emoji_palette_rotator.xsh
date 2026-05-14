# ─────────────────────────────────────────────────────────────
# 🎨 emoji_palette_rotator.xsh — Sources emoji palette by mood
# ─────────────────────────────────────────────────────────────

mood = __xonsh__.env.get('SHELL_MOOD', 'cozy')

emoji_palette_base = "~/projects/my_project/gridiron_gpt/shell/emoji_palette"

palette_map = {
    'cozy': 'diagnostics_fall.xsh',
    'spooky': 'diagnostics_spooky.xsh',
    'affirming': 'diagnostics_spring.xsh',
    'reflective': 'diagnostics_winter.xsh',
}

if mood in palette_map:
    palette_file = os.path.expanduser(f"{emoji_palette_base}/{palette_map[mood]}")
    if os.path.isfile(palette_file):
        print(f"🎨 Loading emoji palette for mood: {mood}")
        source @(palette_file)
    else:
        print(f"⚠️ Emoji palette not found for mood: {mood}")
else:
    print(f"⚠️ No emoji palette mapped for mood: {mood}")
