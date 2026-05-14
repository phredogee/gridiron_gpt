# gridiron_gpt/shell/source_helpers.xsh — GridIron GPT Shell Orchestrator

env = __xonsh__.env

# 🧵 Load modular sourcing helpers
safe_source_glob(f"{env['GRIDIRON_ROOT']}/helpers/source_*.xsh")

# 🧩 Show visual banner
show_gridiron_banner()

# 🚀 Source shell modules with contributor-safe diagnostics
source_if_valid("~/projects/my_project/gridiron_gpt/shell/banner.xsh", "GridIron Banner")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/env_reset.xsh", "Env Reset")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh", "Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/welcome_affirmation.xsh", "Contributor Welcome")

# 🎉 Final affirmations
show_final_affirmations()
