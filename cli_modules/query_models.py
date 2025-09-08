# cli/query_models.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class ParsedQuery:
    domain: str                  # e.g. "nfl"
    position: Optional[str]      # e.g. "WR"
    metric: Optional[str]        # e.g. "targets"
    threshold: Optional[int]     # e.g. 100
    direction: Optional[str]     # e.g. "greater"
    sort_by: Optional[str]       # e.g. "targets"
    limit: Optional[int]         # e.g. 10
    raw_text: str                # original query
