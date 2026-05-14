# gridiron_gpt/helpers/source_diagnostics.xsh
# 🧪 Emoji-coded diagnostics and sourcing trace summary

env = __xonsh__.env

if '__SOURCE_DIAGNOSTICS_LOADED__' not in env:
    env['__SOURCE_DIAGNOSTICS_LOADED__'] = '1'

    def show_source_summary():
        log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_log.txt")
        if not os.path.isfile(log_path):
            print("🧪 No sourcing log found.")
            return

        print("╔════════════════════════════════════════════╗")
        print("║ 🧪 GridIron GPT — Sourcing Summary         ║")
        print("╚════════════════════════════════════════════╝")

        with open(log_path) as f:
            lines = f.readlines()[-10:]  # Show last 10 entries
            for line in lines:
                print(f"🔍 {line.strip()}")

        print("✅ Sourcing diagnostics complete.")
