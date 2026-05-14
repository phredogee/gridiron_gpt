from phred.sports.doctor import diagnose_espn_fetch
from phred.semantic.index import validate_index

def run_diagnostics():
    banner("Running CLI diagnostics...")
    diagnose_espn_fetch()
    validate_index()
