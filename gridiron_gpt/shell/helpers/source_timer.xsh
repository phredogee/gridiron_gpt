# ─────────────────────────────────────────────────────────────
# ⏱️ source_timer.xsh — Logs sourcing duration
# ─────────────────────────────────────────────────────────────

import time

# Start timer
env['SOURCE_START'] = time.time()

# Optional: Print visual breadcrumb
print("⏳ Starting shell sourcing…")

# You’ll source this file *before* your diagnostics and helpers
# Then source_summary.xsh will read SOURCE_START and SOURCE_END

# You can also log intermediate steps like:
# print("📦 Sourcing diagnostics modules…")
