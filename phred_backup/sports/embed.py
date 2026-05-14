# phred/sports/embed.py

import openai
from sentence_transformers import SentenceTransformer

# Load local model once
_local_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_bio(bio, backend="openai"):
    """
    Generate semantic embedding from bio using selected backend.
    Supported: 'openai', 'mistral'
    """
    if not bio:
        return None

    if backend == "openai":
        response = openai.embeddings.create(
            input=bio,
            model="text-embedding-3-small"
        )
        vector = response.data[0].embedding
        return {"vector": vector, "summary": bio}

    elif backend == "mistral":
        # Step 1: Summarize via prompt (stubbed for now)
        summary = summarize_bio(bio)

        # Step 2: Embed summary locally
        vector = _local_model.encode(summary).tolist()
        return {"vector": vector, "summary": summary}

    else:
        raise ValueError(f"Unsupported backend: {backend}")

def summarize_bio(bio):
    """
    Stub: Replace with Mistral prompt logic or local summarizer.
    """
    # For now, just truncate or rephrase slightly
    return bio.strip().split(".")[0] + "."
