# gridiron_gpt/shell/phredenv-reset.xsh

# GridIron GPT Shell Reset

# 🛡️ Defensive session guard
if 'GRIDIRON_SESSION_STARTED' in __xonsh__.env and $GRIDIRON_SESSION_STARTED:
    print("🛡️ Session already started — skipping phredenv-reset.xsh.")
    raise SystemExit

# 🧠 Sourcing fingerprint
timestamp = $(date "+%Y-%m-%d %H:%M:%S")
user = $USER if 'USER' in __xonsh__.env else "unknown"
log_path = "~/projects/my_project/gridiron_gpt/logs/source_trace.log"
log_path = log_path.replace("~", __xonsh__.env["HOME"])
echo f"[{timestamp}] phredenv-reset.xsh sourced by {user}" >> $log_path

# 🔄 Visual banner
print("╔════════════════════════════════════════════════════╗")
print("║ 🔄 GridIron GPT — Shell Reset Module               ║")
print("║ Clears session flags and reloads environment       ║")
print("╚════════════════════════════════════════════════════╝")

print("🔄 Resetting shell environment...")

# 🧹 Clear session flags
__xonsh__.env.pop('__SHELL_HEALTH_CHECK_RUN__', None)
__xonsh__.env.pop('__SHELL_DIAGNOSTICS_RUN__', None)
__xonsh__.env.pop('__GRIDIRON_BANNER_RUN__', None)
__xonsh__.env.pop('__GRIDIRON_SOURCE_HELPERS_RENDERED__', None)
__xonsh__.env.pop('__PHREDENV_DIAGNOSTICS_RUN__', None)

# 🛡️ Safe sourcing
source-safe
source ~/.xonshrc

print("✅ Shell reset complete.")
print("🎉 Environment refreshed. Welcome back, contributor!")
