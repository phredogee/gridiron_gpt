## 🧪 Semantic Feedback Testing

All semantic modules support dry-run diagnostics via `FeedbackContext`. Snapshot tests validate emoji-rich output.

Example:

```python
def test_ingest_diagnostics(snapshot):
    output = ingest_data("data/players.csv", dry_run=True)
    snapshot.assert_match(output, "ingest_feedback")

---

## 📁 Option 2: Create a `docs/` Directory

If you want to scale documentation, create a folder:


---

## 🧰 Option 4: Wire into `dev_activate.sh`

If you want contributors to run a dry-run pipeline on setup, add:

```bash
echo "Running semantic dry-run diagnostics..."
python cli/run_pipeline.py --dry-run --source data/players.csv --query "SELECT * FROM players"
