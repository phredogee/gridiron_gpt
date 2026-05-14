# ~/projects/my_project/gridiron_gpt/shell/contributor_launcher.xsh

# 🛡️ Session guard
if '__CONTRIBUTOR_LAUNCHER_RUN__' not in __xonsh__.env:
    __xonsh__.env['__CONTRIBUTOR_LAUNCHER_RUN__'] = True

    print("🚀 Launching GridIron GPT contributor shell...")

    # 🧼 Source core modules
    source_if_valid("~/projects/my_project/gridiron_gpt/shell/env_reset.xsh", "env_reset")
    source_if_valid("~/projects/my_project/gridiron_gpt/shell/phredenv-loader.xsh", "phredenv-loader")
    source_if_valid("~/projects/my_project/gridiron_gpt/shell/phred_aliases.xsh", "phred_aliases")
    source_if_valid("~/projects/my_project/gridiron_gpt/shell/phredenv-status.xsh", "phredenv-status")
    source_if_valid("~/projects/my_project/gridiron_gpt/pipeline_diagnostics.xsh", "pipeline_diagnostics")

    # 🧪 Run diagnostics
    if 'run_pipeline_diagnostics' in globals():
        run_pipeline_diagnostics()

    # 🌟 Seasonal emoji preview
    if 'rotate_seasonal_emoji' in globals():
        print(f"🌟 Seasonal emoji: {rotate_seasonal_emoji()}")

    # 🎉 Final affirmation
    print("🎉 Contributor shell is online. You are cleared for launch.")
else:
    print("🛡️ Contributor shell already launched — skipping.")
