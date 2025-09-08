# semantic_ingestor/import_audit.py

from semantic_ingestor.feedback import banner_success, banner_error

def audit_imports():
    modules = {
        "normalizers": "semantic_ingestor.normalizers.profile_mapper",
        "ingest_router": "semantic_ingestor.ingest_router",
        # Add more modules here as needed
    }

    for name, path in modules.items():
        try:
            __import__(path)
            banner_success(f"✅ {name} loaded")
        except Exception as e:
            banner_error(f"❌ {name} failed: {e}")
