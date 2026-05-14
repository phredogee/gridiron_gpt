# ~/projects/my_project/gridiron_gpt/shell/gridiron_startup.xsh
# 🚀 GridIron GPT CLI Startup Launcher

import os
env = __xonsh__.env

if '__GRIDIRON_LAUNCHER_RUN__' not in env:
    env['__GRIDIRON_LAUNCHER_RUN__'] = True
    print("🚀 Launching GridIron CLI environment...")

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ 📦 Source core modules                            ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    startup_modules = [
        "env_reset.xsh",
        "phredenv-loader.xsh",
        "doctor.xsh",
        "welcome_affirmation.xsh",
        "../pipeline_diagnostics.xsh"
    ]

    for module in startup_modules:
        path = os.path.expanduser(f"~/projects/my_project/gridiron_gpt/shell/{module}")
        if os.path.isfile(path):
            try:
                execx(f"source {path}")
                print(f"📦 Sourced → {module}")
            except Exception as e:
                print(f"⚠️ Failed to source {module}: {e}")
        else:
            print(f"⚠️ Missing module → {module}")

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ 🩺 Run diagnostics                                ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    try:
        run_pipeline_diagnostics()
        print("🩺 Pipeline diagnostics complete.")
    except Exception as e:
        print(f"❌ Diagnostics failed: {e}")

    print("🌌 GridIron shell is online. You are cleared for launch.")
else:
    print("🛡️ GridIron CLI already launched — skipping startup.")
