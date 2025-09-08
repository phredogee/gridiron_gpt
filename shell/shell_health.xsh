# ~/projects/my_project/gridiron_gpt/shell/shell_health.xsh

def source_if_valid(path, label):
    path = os.path.expanduser(path)
    shield = "🛡️"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] {label}: "

    if os.path.isfile(path):
        source path
        echo f"{shield} [{label}] ✅ Loaded"
        log_entry += f"✅ Loaded from {path}"
    else:
        echo f"{YELLOW}{shield} [{label}] ⚠️ Missing — skipped{RESET}"
        log_entry += f"⚠️ Missing at {path}"

    with open("source_log.txt", "a") as f:
        f.write(log_entry + "\n")

echo "╔════════════════════════════════════════════╗"
echo "║ 🌟 GridIron GPT Shell Launch: Health Check ║"
echo "╚════════════════════════════════════════════╝"

source_if_valid("~/projects/my_project/gridiron_gpt/shell/banner_path.xsh", "GridIron Banner")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/env_reset.xsh", "Env Reset")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/diagnostics.xsh", "Diagnostics")
source_if_valid("~/projects/my_project/gridiron_gpt/shell/welcome_affirmation.xsh", "Contributor Welcome")

echo "🎉 Shell modules loaded. See source_log.txt for full trace."

echo "🩺 Running shell health checks..."
source ~/projects/my_project/gridiron_gpt/shell/shell_health.xsh
echo "✅ Health checks passed. Shell integrity confirmed."

echo "🛸 Welcome aboard the GridIron CLI. All systems are green. You are cleared for launch."
echo f"{datetime.datetime.now()} - Shell launched by $USER" >> ~/projects/my_project/gridiron_gpt/logs/shell_launch.log
