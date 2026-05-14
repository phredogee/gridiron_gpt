# gridiron_gpt/semantic_query.py
def run_query(query: str):
    """Parse a very limited SQL-like SELECT statement for testing."""
    query = query.strip()
    if not query.upper().startswith("SELECT "):
        raise ValueError(f"Unsupported query: {query}")

    value = query[7:].strip()

    # Handle NULL
    if value.upper() == "NULL":
        return None

    # Handle quoted strings
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]

    # Handle integers
    if value.isdigit():
        return int(value)

    # Fallback: return as-is
    return value
