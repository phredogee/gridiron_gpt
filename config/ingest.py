# ingest.py

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PlayerProfile:
    name: str
    position: str
    team: str
    opponent: str
    matchup_rating: Optional[float] = None
    injury_status: Optional[str] = None
    notes: Optional[str] = None

def load_sample_profiles() -> List[PlayerProfile]:
    return [
        PlayerProfile(
            name="Christian McCaffrey",
            position="RB",
            team="49ers",
            opponent="Rams",
            matchup_rating=0.85,
            injury_status="Healthy",
            notes="Elite PPR upside"
        ),
        PlayerProfile(
            name="Joe Mixon",
            position="RB",
            team="Bengals",
            opponent="Steelers",
            matchup_rating=0.45,
            injury_status="Healthy",
            notes="Tough run defense matchup"
        ),
        # Add more profiles as needed
    ]
