"""
🧭 Walkthrough: How query logic works in gridiron_gpt

This module is designed to help new contributors understand:
- How to write basic query tests
- What to expect from run_query
- How to handle errors gracefully
"""

import pytest
from gridiron_gpt.query import run_query  # Adjust as needed

def test_simple_query():
    result = run_query("SELECT 1")
    assert result == 1
    print("✅ Basic query returned expected result")

def test_query_with_explanation():
    """
    This test shows how to assert expected output and explain why it matters.
    """
    result = run_query("SELECT 2")
    assert result == 2, "We expect SELECT 2 to return 2 — sanity check"
    print("✅ SELECT 2 returned 2 as expected")

def test_error_handling():
    """
    Demonstrates how to test for invalid input and raise meaningful errors.
    """
    with pytest.raises(ValueError):
        run_query("DROP DATABASE")  # Should be blocked
    print("✅ Invalid query correctly raised ValueError")
