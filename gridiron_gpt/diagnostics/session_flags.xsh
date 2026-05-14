# gridiron_gpt/shell/session_flags.xsh
# 🛡️ Defensive session flag setup

if 'GRIDIRON_SESSION_STARTED' not in __xonsh__.env:
    $GRIDIRON_SESSION_STARTED = False

if '__SHELL_HEALTH_CHECK_RUN__' not in __xonsh__.env:
    __xonsh__.env['__SHELL_HEALTH_CHECK_RUN__'] = '0'

if '__GRIDIRON_LAUNCHER_RUN__' not in __xonsh__.env:
    __xonsh__.env['__GRIDIRON_LAUNCHER_RUN__'] = '0'

# 🧠 GridIron GPT — Session Flags Initialized
# This module sets default flags for shell health and launcher tracking.
# It is safe to source multiple times and does not echo or log.
