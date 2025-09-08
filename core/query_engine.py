# gridiron_gpt/core/query_engine.py

from sentence_transformers import SentenceTransformer
import faiss

class QueryEngine:
    def __init__(self, advisor):
        self.advisor = advisor
        self.model = advisor.model
        self.index = advisor.index
        self.documents = advisor.documents

    def search(self, query, top_k=5):
        print(f"🔍 Searching for: {query}")
        query_embedding = self.model.encode([query])
        scores, indices = self.index.search(query_embedding, top_k)
        results = [self.documents[i] for i in indices[0]]
        return results
