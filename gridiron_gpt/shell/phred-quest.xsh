# gridiron_gpt/shell/phred-quest.xsh — GridIron GPT Contributor Quest Module

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and __xonsh__.env['GRIDIRON_SESSION_STARTED']:
    print("🛡️ Session already started — skipping phred-quest.xsh.")
    raise SystemExit

# 🛡️ Prevent duplicate rendering
if '__PHRED_QUEST_RUN__' in __xonsh__.env:
    print("🌟 Contributor quests already surfaced — skipping.")
    raise SystemExit

__xonsh__.env['__PHRED_QUEST_RUN__'] = '1'

# 🧠 Sourcing fingerprint
from datetime import datetime
import os

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = __xonsh__.env.get("USER", "unknown")
log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_trace.log")

with open(log_path, "a") as f:
    print(f"[{timestamp}] phred-quest.xsh sourced by {user}", file=f)

# 🧭 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🧭 GridIron GPT — Contributor Quest Module         ║")
print("║ Surfaces active quests and onboarding challenges   ║")
print("╚════════════════════════════════════════════════════╝")

# 🌟 Quest Tips (stubbed for now
