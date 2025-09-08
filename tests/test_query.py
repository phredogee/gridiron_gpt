
import pytest
from gridiron_gpt.scripts.dry_run_matchup import run_matchup_query  # Adjust if needed
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print("🛠️ Injected project root into sys.path for test discovery.")

def test_basic_query():
    result = run_matchup_query("SELECT 1")
    assert result == 1  # Replace with actual expected output

@pytest.mark.parametrize("query,expected", [
    ("SELECT 0", 0),
    ("SELECT NULL", None),
    ("SELECT 'text'", "text"),
])

def test_query_edge_cases(query, expected):
    result = run_query(query)
    assert result == expected
    print(f"✅ Query `{query}` returned `{expected}` as expected")

def test_parametrized_queries(query, expected):
    result = run_matchup_query(query)
    assert result == expected

def test_invalid_query():
    with pytest.raises(Exception):
        run_matchup_query("DROP TABLE users")  # Or whatever should fail

def test_feedback():
    result = run_matchup_query("SELECT 1")
    if result == 1:
        print("✅ Query returned expected result")
    else:
        print("❌ Unexpected query result")
    assert result == 1
