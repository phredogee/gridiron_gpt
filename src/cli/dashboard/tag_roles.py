# src/cli/dashbaord/tag_roles.py

from typing import List, Dict
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Define role archetypes and their embedding anchors
ROLE_TAGS = {
    "Route Runner": [0.12, 0.88, 0.34, ...],  # example embedding
    "Dual-Threat QB": [0.45, 0.22, 0.91, ...],
    "Ball Hawk": [0.78, 0.11, 0.56, ...],
    # Add more roles as needed
}

def tag_roles(players, role_tags, embedding_key="embedding"):
    role_names = list(role_tags.keys())
    role_vectors = np.array(list(role_tags.values()))

    for p in players:
        emb = np.array(p.get(embedding_key))
        if emb is None or len(emb) != len(role_vectors[0]):
            p["role_tag"] = "Unknown"
            continue

        sims = cosine_similarity([emb], role_vectors)[0]
        best_idx = int(np.argmax(sims))
        p["role_tag"] = role_names[best_idx]

    return players

if __name__ == "__main__":
    mock_players = [
        {"name": "Nick Bosa", "embedding": [0.77, 0.12, 0.55, ...]},
        {"name": "Lamar Jackson", "embedding": [0.44, 0.23, 0.90, ...]},
    ]
    tagged = tag_roles(mock_players)
    for p in tagged:
        print(f"🔹 {p['name']} → {p['role_tag']}")
