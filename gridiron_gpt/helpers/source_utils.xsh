# ~/.xonshrc.d/helpers/source_utils.xsh — Contributor UX helpers 🌟

env = __xonsh__.env

if '__SOURCE_UTILS_LOADED__' not in env:
    env['__SOURCE_UTILS_LOADED__'] = '1'
    print("🧩 Entering source_utils.xsh — contributor UX helpers loaded.")

    # 🧩 Contributor aliases (only if functions are defined)
    if 'source_safe' in globals():
        aliases['source-safe'] = source_safe
    else:
        print("⚠️ source_safe not defined — alias skipped.")

    if 'show_source_summary' in globals():
        aliases['source-summary'] = show_source_summary
    else:
        print("⚠️ show_source_summary not defined — alias skipped.")

    # 🌟 Contributor welcome alias
    def welcome_contributor():
        print("╔════════════════════════════════════════════╗")
        print("║ 🌟 Welcome to GridIron GPT Shell           ║")
        print("║ You’re now sourcing like a contributor!    ║")
        print("╚════════════════════════════════════════════╝")

    aliases['welcome'] = welcome_contributor

    # 🧵 Source report alias (optional)
    def source_report():
        log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/source_log.txt")
        if not os.path.isfile(log_path):
            print("🧪 No sourcing log found.")
            return

        print("╔════════════════════════════════════════════╗")
        print("║ 📦 GridIron GPT — Source Report            ║")
        print("╚════════════════════════════════════════════╝")

        with open(log_path) as f:
            for line in f:
                print(f"📦 {line.strip()}")

    aliases['source-report'] = source_report
