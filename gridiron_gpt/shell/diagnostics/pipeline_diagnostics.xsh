# gridiron_gpt/pipeline_diagnostics.xsh

# ┌────────────────────────────────────────────┐
# │ 🧪 NFL Pipeline Diagnostics                │
# └────────────────────────────────────────────┘

from datetime import datetime
import os
env = __xonsh__.env

def run_pipeline_diagnostics(seasons=None):
    # 🛡️ Session guard
    if env.get('__PIPELINE_DIAGNOSTICS_RUN__'):
        print("🏈 Pipeline diagnostics already run — skipping.")
        return
    env['__PIPELINE_DIAGNOSTICS_RUN__'] = True

    # 🧠 Default seasons
    if seasons is None:
        seasons = [2022, 2023]

    # 🧠 Sourcing fingerprint
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = env.get("USER", "unknown")
    log_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/logs/pipeline_diagnostics.log")

    try:
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] Ran diagnostics for seasons: {seasons} by {user}\n")
    except Exception as e:
        print(f"⚠️ Failed to write sourcing log: {e}")

    # 🧪 Banner
    print("╔════════════════════════════════════════════╗")
    print("║ 🏈 GridIron GPT NFL Pipeline Diagnostics   ║")
    print("╚════════════════════════════════════════════╝")
    print("🧪 Running NFL pipeline diagnostics...")

    # 🧼 Import pipeline functions
    try:
        from data_pipeline import get_pbp, get_player_stats
    except ImportError as e:
        print(f"🛑 Failed to import pipeline functions: {e}")
        return

    # 📦 Load play-by-play data
    try:
        pbp = get_pbp(seasons)
        print(f"📦 PBP records loaded: {len(pbp)}")
    except Exception as e:
        print(f"🛑 Failed to load PBP data: {e}")

    # 📦 Load player stats
    try:
        stats = get_player_stats(seasons)
        print(f"📦 Player stats loaded: {len(stats)}")
    except Exception as e:
        print(f"🛑 Failed to load player stats: {e}")

    # 🎉 Final affirmation
    print("🎉 NFL pipeline diagnostics complete. Shell is contributor-ready.")
    
    #    Stage diagnostics
    print("📊 Stage Diagnostics:")
    if env.get("FETCH_SUCCESS"):
        print("✅ Data fetched successfully! 🏈")
    else:
        print("⚠️ Fetch incomplete or failed.")

    if env.get("VALIDATION_PASS"):
        print("🧪 Validation passed. Schema looks solid!")
    else:
        print("🚨 Validation failed. Check formats and types.")

    if env.get("PARSE_COMPLETE"):
        print("📦 Parsing complete. Ready for summary.")
    else:
        print("🧩 Parsing incomplete. Check for missing keys.")

    source helpers/visuals/emoji_rotation.xsh
    $emoji = $(pick_rotating_emoji)
    print(f"{emoji} Diagnostics complete. Contributors make the play!")

    env['DIAGNOSTIC_SEASONS'] = seasons
