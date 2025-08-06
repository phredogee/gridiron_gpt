from project_gridiron_gpt.pipelines import build_pipelines

def ingest_all():
    data = build_pipelines()
    # Save to disk, DB, or pass to downstream modules
