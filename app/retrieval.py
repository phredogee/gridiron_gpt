# app/retrieval.py

from embed import get_embeddings  # Assuming you have a function like this
import faiss
import numpy as np
from config.settings import EMBEDDING_DIM
...
self.index = faiss.IndexFlatL2(EMBEDDING_DIM)

class SemanticRetriever:
    def __init__(self, dim=384):  # Adjust based on your embedding model
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def build_index(self, texts):
        embeddings = get_embeddings(texts)
        self.index.add(np.array(embeddings))
        self.metadata = texts

    def search(self, query, top_k=5):
        query_vec = np.array(get_embeddings([query]))
        distances, indices = self.index.search(query_vec, top_k)
        return [(self.metadata[i], distances[0][idx]) for idx, i in enumerate(indices[0])]
