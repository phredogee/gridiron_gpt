# GridironGPT

A fantasy football analytics CLI that fetches NFL player data from ESPN, validates and indexes it with FAISS + sentence transformers, and surfaces rankings and recommendations through a Click-based command interface.

## Features

- **ESPN data pipeline** — fetches, cleans, and validates weekly player stats
- **Semantic advisor** — embeds player documents with `sentence-transformers` and indexes them in FAISS for similarity search
- **Ranking pipeline** — scores and ranks players from ingested ESPN data
- **CLI** — `espn intake`, `espn dry-run`, and `espn fix` commands with dry-run support throughout
- **Feedback system** — scoped emoji-rich logging via `FeedbackContext`

## Requirements

- Python 3.11+
- See `requirements.txt` for full dependency list (includes `torch`, `faiss-cpu`, `sentence-transformers`, `nflreadpy`)

## Installation

```bash
git clone git@github.com:phredogee/gridiron_gpt.git
cd gridiron_gpt
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Set Python path so the package resolves correctly
export PYTHONPATH=$(pwd)/..

# Ingest ESPN data for a given week
python -m gridiron_gpt espn intake --week 5

# Preview without saving
python -m gridiron_gpt espn intake --week 5 --dry-run

# Scan for missing player entries
python -m gridiron_gpt espn fix --week 5

# Preview ESPN intake and validate structure
python -m gridiron_gpt espn dry-run --week 5
```

## Project Structure

```
gridiron_gpt/
├── __main__.py                 # Entry point: python -m gridiron_gpt
├── cli/
│   ├── main.py                 # Click group root
│   └── espn.py                 # ESPN subcommands (intake, dry-run, fix)
├── core/
│   └── advisor.py              # FAISS + sentence-transformers semantic engine
├── data_ingest/
│   └── espn_ingest.py          # ESPN API fetch, clean, save
├── semantic/
│   └── espn_ingest.py          # Orchestrates ingest + validation
├── validators/
│   └── profile_validator.py    # Schema validation for player profiles
├── pipelines/
│   └── ranking_pipeline.py     # Player ranking logic
├── feedback/
│   └── __init__.py             # Banner/logging helpers
├── data_pipeline.py            # nflreadpy wrappers (play-by-play, player stats)
└── tests/                      # 74 tests across CLI, pipeline, feedback, ingestion
```

## Running Tests

```bash
export PYTHONPATH=$(pwd)/..
pytest tests/ -v
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `PYTHONPATH` | Must include the parent of `gridiron_gpt/` for imports to resolve |
| `HF_TOKEN` | Optional — suppresses Hugging Face rate-limit warnings |
