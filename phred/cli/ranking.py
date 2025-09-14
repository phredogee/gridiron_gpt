# phred/cli/ranking.py

def generate_rankings(dry_run=False):
    """
    Generate player/team rankings.

    Args:
        dry_run (bool): If True, return dummy data for testing.

    Returns:
        list: A list of ranking entries.
    """
    if dry_run:
        # Dummy data for testing
        return [
            {"rank": 1, "name": "Player One", "score": 99},
            {"rank": 2, "name": "Player Two", "score": 95},
        ]

    # TODO: Implement real ranking logic here
    raise NotImplementedError("Live ranking generation not implemented yet")
