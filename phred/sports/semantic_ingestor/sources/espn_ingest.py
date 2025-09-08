# semantic_ingestor/sources/espn_ingest.py
import pandas as pd

def fetch_espn_data(url: str) -> pd.DataFrame:
    """Fetch raw ESPN data from a given URL."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        raise RuntimeError(f"🛑 ESPN ingest failed: {e}")
