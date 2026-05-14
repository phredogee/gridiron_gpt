# 🏈 Gridiron GPT — ESPN Pipeline CLI

Welcome to the **Phred CLI Ecosystem**, where every fetch, merge, and semantic audit is built to teach and empower. This repo scaffolds ESPN-style player pipelines with dry-run diagnostics, contributor-friendly fetchers, and expressive CLI feedback.

---

## 🧪 Running the CLI

```bash
./run_zodiac.sh --year 1992

# ESPN dry-run mode:
# python -m phred.cli.run_pipeline --season 2025 --dry-run #
# ===========================================================

#ESPN Dry-Run Pipeline Flow:
# fetch_from_espn(dry_run=True)
#         ↓
# get_player_bios(players, dry_run=True)
#         ↓
# align_embeddings(players, bios)
#         ↓
# 🧠 Semantic audit + CLI feedback

# Running Tests:
export PYTHONPATH=$(pwd)
pytest gridiron_gpt/tests/test_espn_pipeline.py

#Repo Structure:
# gridiron_gpt/
# ├── phred/
# │   ├── sports/
# │   │   ├── fetch.py
# │   │   ├── espn.py
# │   │   └── ...
# │   ├── cli/
# │   │   ├── run_pipeline.py
# │   │   └── ...
# ├── tests/
# │   └── test_espn_pipeline.py
