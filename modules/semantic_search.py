import requests
import faiss
import numpy as np

def embed_texts(texts, mistral_url="http://localhost:8000/embed"):
    """
    Sends a list of texts to the Mistral embedding API and returns embeddings.
    """
    response = requests.post(mistral_url, json={"texts": texts})
    response.raise_for_status()
    return response.json()["embeddings"]

def build_index(embeddings):
    """
    Builds a FAISS index from a list of embeddings.
    """
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def query_index(index, query_text, mistral_url="http://localhost:8000/embed", top_k=5):
    """
    Embeds the query text and returns top_k matching indices from the FAISS index.
    """
    query_vec = embed_texts([query_text], mistral_url)[0]
    _, indices = index.search(np.array([query_vec]), top_k)
    return indices[0]

if __name__ == "__main__":
    sample_texts = ["Justin Jefferson WR MIN", "Bijan Robinson RB ATL", "CJ Stroud QB HOU"]
    embeddings = embed_texts(sample_texts)
    index = build_index(embeddings)
    results = query_index(index, "rookie RBs with upside")
    print("Top matches:", [sample_texts[i] for i in results])

# semantic_search.py

def run_semantic_query(players, index, query, mistral_url="http://localhost:8000/embed"):
    """
    Runs a semantic query over the FAISS index and returns matching players.
    """
    top_indices = query_index(index, query, mistral_url)
    return [players[i] for i in top_indices]

print(f"🔍 Query embedded with {provider} — searching index...")
