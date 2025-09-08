# my_project/gridiron_gpt/query.py

def run_query(query: str):
    """
    Parse a very limited SQL-like SELECT statement for testing purposes.

    Supported patterns:
      SELECT <integer>       -> returns int
      SELECT NULL            -> returns None
      SELECT '<string>'      -> returns string without quotes

    Raises:
      ValueError for unsupported or unsafe queries.
    """
    if not isinstance(query, str):
        raise TypeError(f"Query must be a string, got {type(query).__name__}")

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

    # If it doesn't match any known safe pattern, block it
    raise ValueError(f"Unsupported SELECT value: {value}")
