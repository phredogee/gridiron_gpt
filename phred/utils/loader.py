# phred/utils/loader.py

def load_cleaned_data(source=None, dry_run=False):
    """
    Load cleaned data from a given source.
    In dry_run mode, return dummy data for testing.
    """
    if dry_run:
        # Dummy cleaned data for testing
        return [
            {"id": 1, "text": "Sample record one", "label": "A"},
            {"id": 2, "text": "Sample record two", "label": "B"},
        ]

    # TODO: Implement real data loading logic here
    # For example: read from a file, database, or API
    raise NotImplementedError("Live data loading not implemented yet")
