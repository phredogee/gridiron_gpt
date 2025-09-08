# ~/projects/my_project/gridiron_gpt/phredenv/reset.xsh 🪄

import os
import datetime

if 'PROJECT_ROOT' not in __xonsh__.env:
    PROJECT_ROOT = '/home/phredo/projects/my_project/gridiron_gpt'
    print(f"📁 PROJECT_ROOT not set. Using default: {PROJECT_ROOT}")

folders = ['shell', 'phredenv', 'modules']
missing = [f for f in folders if not os.path.isdir(os.path.join(PROJECT_ROOT, f))]

if missing:
    print(f"⚠️ Missing folders: {', '.join(missing)}")
else:
    print("📁 All required folders are present.")

print(f"📦 Sourcing env.xsh from: {os.path.join(PROJECT_ROOT, 'phredenv/env.xsh')}")
execx(f"source {os.path.join(PROJECT_ROOT, 'phredenv/env.xsh')}")
execx(f"source {os.path.join(PROJECT_ROOT, 'phredenv/health.xsh')}")

print("🔄 Resetting phred environment...")
try:
    run_reset()
except Exception as e:
    print(f"❌ Reset failed: {e}")

execx("source ~/.xonshrc")
print("✅ Environment reloaded. Welcome back, contributor!")
print(f"🕒 Reset triggered at: {datetime.datetime.now()}")
