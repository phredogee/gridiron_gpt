
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from semantic.router import route_query

from gridiron_gpt.semantic.router import route_query

def test_route_query_dry_run():
    from gridiron_gpt.semantic.router import route_query
    queries = [
        "Show me rushing yards for Christian McCaffrey",
        "How many receiving yards did Tyreek Hill have?",
        "Who had the most touchdowns last week?"
    ]
    for q in queries:
        result = route_query(q, dry_run=True)
        assert result is not None
