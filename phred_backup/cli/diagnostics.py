# phred/cli/diagnostics.py

from phred.diagnostics.core import diagnose_generic
from phred.sports.espn_diagnostics import diagnose_espn_fetch

def semantic_diagnose():
    print("🧠 Running semantic diagnostics...")
    diagnose_generic()
    diagnose_espn_fetch()
