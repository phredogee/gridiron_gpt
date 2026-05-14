# ─────────────────────────────────────────────────────────────
# 🎭 source_mood.xsh — Sets shell mood for seasonal theming
# ─────────────────────────────────────────────────────────────

from datetime import datetime

week = datetime.now().isocalendar()[1]

# Rotate mood based on week number
if week % 4 == 0:
    __xonsh__.env['SHELL_MOOD'] = 'cozy'
elif week % 4 == 1:
    __xonsh__.env['SHELL_MOOD'] = 'spooky'
elif week % 4 == 2:
    __xonsh__.env['SHELL_MOOD'] = 'affirming'
else:
    __xonsh__.env['SHELL_MOOD'] = 'reflective'

print(f"🎭 Shell mood set to: {__xonsh__.env['SHELL_MOOD']}")
