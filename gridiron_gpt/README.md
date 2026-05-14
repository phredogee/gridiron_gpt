---

### 🧭 Contributor Tip

To reinforce clarity, scaffold a mapping table in your README or onboarding docs:

| Symbol             | Import Path                | Purpose                          |
|--------------------|----------------------------|----------------------------------|
| `FeedbackContext`  | `phred.feedback`           | Scoped emoji-rich logging        |
| `banner()`         | `phred.utils.banner_utils` | Quick one-line CLI feedback      |
| `render()`         | Method on `FeedbackContext`| Joins logs for display           |

---

gridiron_gpt/
├── __init__.py
├── core/
│   ├── __init__.py
│   └── advisor.py              # Semantic engine: embedding, indexing, save/load
├── pipelines/
│   ├── __init__.py
│   ├── builder.py              # Orchestrates all pipeline runs
│   ├── injury_pipeline.py      # Ingests injury data, builds index
│   ├── matchup_pipeline.py     # (Assumed) Ingests weekly matchups
│   ├── news_pipeline.py        # Ingests NFL news articles
│   ├── projection_pipeline.py  # Ingests player projections
│   ├── ranking_pipeline.py     # Ingests player rankings
│   └── custom_advice_pipeline.py # Synthesizes advice from multiple sources
├── data/
│   └── ...                     # Any raw or processed data files
├── assets/
│   └── ...                     # Optional: logos, icons, etc.
├── tests/
│   └── test_query.py   
└── index_rebuilt.index         # FAISS index saved by Advisor

~/phredo/my_project/
├── run_pipelines.sh                  ✅ Existing shell script
├── logs/                             📁 Log files
├── gridiron_gpt/
│   ├── pipelines/                    📁 Your ingestion logic
│   └── triggers/                     🆕 Optional: new folder for Flask + Slack logic
│       ├── flask_trigger.py          🧠 Flask API to run pipeline
│       └── slack_notifier.py         🔔 Sends Slack messages with buttons
│       └── config.py                 🔔 Stores webhook URLs, endpoints, etc.

What’s Working
- ✅ `phred/sports/espn.py` and `espn_dry_run.py` removed — ESPN logic now lives in `phred/sports/fetchers/espn.py`. All registry and test references updated.
- FAISS Indexing: save_index() is functioning across multiple pipelines.
- Pipeline Execution: Each module (injury, ranking, news, projection, custom_advice) is running without crashing.
- Semantic Advisor: Your Advisor class is now properly saving and reusing indexes.
- Terminal Output: Clear, expressive logs — I love the use of emojis for readability.

⚠️ Minor Warnings
- runpy RuntimeWarning: This is benign. It’s just Python warning you that the module was already loaded before execution. You can ignore it unless you’re doing dynamic reloading.
- encoder_attention_mask Deprecation: This is from HuggingFace’s transformers library. It’s warning that encoder_attention_mask will be removed in v4.55.0. You’re likely fine unless you’re customizing attention logic.

📦 ESPN Module Migration
- Legacy `phred.sports.espn` deprecated.
- Use `phred.sports.fetchers.espn` for all ESPN-related hooks and fetch logic.
- Registry entries and CLI diagnostics updated accordingly.

## 🧹 Module Cleanup

- ✅ `phred/sports/espn.py` and `espn_dry_run.py` removed — ESPN logic now lives in `phred/sports/fetchers/espn.py` for modular clarity.
- 🔄 Registry and dynamic imports updated to reflect new path.
- 📘 Contributor docs patched to reference `fetchers.espn`.

## 📦 Packaging Refreshed

- 🧼 `.egg-info` metadata rebuilt to remove stale references.
- ✅ Wheel built successfully: `phred-0.1.0-py3-none-any.whl`
- 🧪 Future-proofing: consider adding `phred doctor packaging` to audit manifest paths and build hygiene.

## 🧪 Coming Soon: `phred doctor`

- ✅ Validates semantic hook imports
- 🧼 Audits deprecated modules and packaging artifacts
- 🔍 Prints emoji-tiered feedback for onboarding clarity

### 🧠 Importing Feedback Helpers

### Using `FeedbackContext`

```python
from phred.feedback import FeedbackContext

with FeedbackContext("success") as ctx:
    ctx.log("Setup complete")
    print(ctx.render())


#### ✅ Part 2: Developer Setup

```markdown
### Developer Environment Setup

```bash
chmod +x dev_activate.sh
./dev_activate.sh

git tag -a v0.1.0 -m "Initial dev setup and SSH fix"
git push origin v0.1.0

## 🧠 Semantic Pipeline Overview

This project uses an expressive, emoji-rich feedback system powered by `FeedbackContext`. Each semantic step—querying, ingestion, validation, transformation—is wrapped in diagnostics that support dry-run mode and snapshot testing.

### Example Usage

```python
from phred.semantic.query_engine import run_query
result = run_query("SELECT * FROM players", dry_run=True)
print(result.render())

## 🧠 Shell Onboarding (phredenv)

GridIron GPT includes a modular shell environment powered by Xonsh. It’s designed for contributor clarity, emoji-rich diagnostics, and session hygiene.

### 🧪 Loader Architecture

The shell uses a centralized `load_file(path, label)` function to handle all startup sourcing. It supports:

| File Type | Loader Used        | Diagnostic Banner                    |
|-----------|--------------------|--------------------------------------|
| `.xsh`    | `source path`      | 📦 Loading `{label}` → `path`        |
| `.sh`     | `source-bash path` | 🧼 Sourcing Bash script → `path`     |
| `.py`     | `python3 path`     | 🐍 Executing Python loader → `path`  |

Each loader is wrapped in `try/except` blocks to affirm contributors and catch edge cases.

### 🛡️ Session Guards

To prevent double-sourcing and banner duplication, the shell uses scoped environment flags:

- `PHREDENV_BANNER_SHOWN`
- `__GRIDIRON_SOURCE_HELPERS_RENDERED__`
- `__HEALTH_CHECK_LOADED__`

These ensure each module loads once per session.

### 🛠️ Aliases

Aliases are defined in a guarded block and include:

- `phred-reset`: Reloads the environment
- `source-safe`: Sources helper utilities
- `gc`: Commits with a message
- `refresh-shell`: Reloads `.xonshrc`

You can extend aliases inside the `__ALIASES_LOADED__` block.

### 🩺 Diagnostics & Health Checks

The shell automatically sources:

- `shell_health.xsh`: Environment sanity checks
- `doctor.xsh`: Contributor diagnostics
- `pipeline_diagnostics.xsh`: NFL pipeline readiness

Each is loaded once per session using `load_file()` or `source_if_valid()`.

### 🌌 Welcome Sequence

Every shell launch includes:

- Timestamped launch message
- Visual shields (Red, Blue, Gold)
- CLI version, registry, and test status
- Contributor tips and commands

This sequence affirms contributors and sets the tone for a productive session.

---

### 🧪 Extending the Shell

To add new modules:

1. Drop your `.xsh`, `.sh`, or `.py` file into the appropriate folder.
2. Define its path in `.xonshrc`.
3. Call `load_file(path, "Your Label")` inside a guarded block.

To add new diagnostics:

- Use `source_if_valid(path, label)` for modular sourcing.
- Wrap in session guards to prevent duplication.

---

### 🧭 Contributor Tip

To reinforce clarity, scaffold a mapping table in your README or onboarding docs:

| Symbol             | Import Path                | Purpose                          |
|--------------------|----------------------------|----------------------------------|
| `FeedbackContext`  | `phred.feedback`           | Scoped emoji-rich logging        |
| `banner()`         | `phred.utils.banner_utils` | Quick one-line CLI feedback      |
| `render()`         | Method on `FeedbackContext`| Joins logs for display           |
