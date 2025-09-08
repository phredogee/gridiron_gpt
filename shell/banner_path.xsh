# banner_path.xsh

$banner_path = "~/projects/my_project/gridiron_gpt/shell/banner_path.xsh"
$banner_path = os.path.expanduser($banner_path)

if os.path.isfile($banner_path):
    source $banner_path
    echo f"🌟 Banner logic sourced from {$banner_path}"
else:
    echo f"{YELLOW}📭 banner_path.xsh not found at {$banner_path} — skipping{RESET}"

def source_if_valid(path, label):
    path = os.path.expanduser(path)
    shield = "🛡️"
    if os.path.isfile(path):
        source path
        echo f"{shield} [{label}] ✅ Loaded from {path}"
    else:
        echo f"{YELLOW}{shield} [{label}] ⚠️ Missing at {path} — skipped{RESET}"

source_if_valid("~/projects/my_project/gridiron_gpt/shell/banner_path.xsh", "GridIron Banner Logic")

echo "🚀 Launching GridIron GPT Shell Modules"

source_if_valid("~/projects/my_project/gridiron_gpt/shell/banner_path.xsh", "GridIron Banner")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/env_reset.xsh", "Env Reset")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh", "Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/welcome_affirmation.xsh", "Contributor Welcome")

echo "🎉 All available modules sourced. Shell is contributor-ready."

echo "╔════════════════════════════════════════════╗"
echo "║ 🌟 Welcome to gridiron_gpt contrib. shell  ║"
echo "╚════════════════════════════════════════════╝"
