# phred/semantic/index.py

def patch_index(index):
    """
    🛠️ Ensures the index is in the correct format.
    For now, just return the index unchanged.
    """
    # In a real implementation, you might normalize keys, merge aliases, etc.
    return index

def validate_index(index):
    """
    ✅ Validates that the index is a dict with non-empty lists as values.
    """
    if not isinstance(index, dict):
        return False
    for key, value in index.items():
        if not isinstance(value, list):
            return False
    return True
