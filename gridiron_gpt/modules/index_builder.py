def store_vector(vec, metadata, provider="mistral"):
    record = {
        "embedding": vec,
        "provider": provider,
        "metadata": metadata
    }
    # Save to disk or DB
