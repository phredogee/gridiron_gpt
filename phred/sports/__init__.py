# phred/sports/__init__.py

# phred/sports/__init__.py

from .espn import fetch_from_espn
from phred.feedback import banner, feedback_context  # ✅ import working implementations

__all__ = ["fetch_from_espn", "banner", "feedback_context"]
