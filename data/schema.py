# data/schema.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class PlayerProfile:
    name: str
    position: str
    team: str
    opponent: str
    matchup_rating: Optional[float] = None  # e.g. 0.0 (bad) to 1.0 (great)
    injury_status: Optional[str] = None     # e.g. "Healthy", "Questionable", "Out"
    notes: Optional[str] = None             # Freeform advice or scouting notes
