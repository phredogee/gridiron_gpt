# core/advisor.py
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from gridiron_gpt.core.utils import load_index_from_file, save_index, load_documents_from_file, embed_documents

class Advisor:
    def __init__(self, index_path="index_rebuilt.index"):
        self.index_path = index_path
        self.embeddings = None
        self.documents = []
        self.index = faiss.IndexFlatL2(384)  # Adjust if using different embedding dim
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, texts):
        return self.model.encode(texts, normalize_embeddings=True)

    def add_documents(self, texts, embeddings):
        print(f"📄 Adding {len(texts)} documents to index...")

        if embeddings is None:
            embeddings = self.model.encode(texts)

        self.index.add(embeddings)
        self.documents = texts
        self.embeddings = embeddings

        print("✅ Documents embedded and indexed.")

    def ingest(self):
        texts = [
            "Justin Jefferson is expected to play",
            "Bijan Robinson is a top RB this week",
            "Jordan Addison could be a sleeper pick",
        ]
        embeddings = self.embed(texts)
        self.add_documents(texts)
        self.save_index(self.index_path)
        print(f"✅ FAISS index saved to {self.index_path}")

    def ingest_documents(self, source_path):
        print(f"📄 Loading documents from: {source_path}")
        self.documents = load_documents_from_file(source_path)
        self.embeddings = embed_documents(self.documents)
        self.rebuild_index()

    def rebuild_index(self):
        if self.embeddings is None:
            raise ValueError("Embeddings must be initialized before rebuilding index.")
        print(f"🔄 Rebuilding index with {len(self.embeddings)} documents...")
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.index.add(self.embeddings.astype(np.float32))
        save_index(self.index, self.index_path)
        print(f"💾 Rebuilt index saved to: {self.index_path}")

    def load_index(self):
        print(f"📥 Loading index from: {self.index_path}")
        self.index = load_index_from_file(self.index_path)
        if self.index is None:
            raise FileNotFoundError(f"Index file not found: {self.index_path}")
        print("✅ Index loaded successfully.")

    @property
    def embedding_dim(self):
        if self.embeddings is None:
            raise ValueError("Embeddings not initialized yet.")
        return self.embeddings.shape[1]

    def compute_query_embedding(self, text):
        return self.embed([text]).astype("float32").reshape(1, -1)

    def query(self, text, top_k=3):
        if self.index is None:
            raise RuntimeError("Index not loaded. Call load_index() first.")
        query_embedding = self.compute_query_embedding(text)
        distances, indices = self.index.search(query_embedding, top_k)

        print(f"\n🔍 Query: {text}")
        print(f"📊 Top {top_k} results:")
        for i, (idx, dist) in enumerate(zip(indices[0], distances[0])):
            result_text = self.documents[idx] if idx < len(self.documents) else f"Index #{idx}"
            print(f"  {i+1}. {result_text} — Distance: {dist:.4f}")
        
    def save_index(self, path=None):
        save_path = path or self.index_path
        if self.index is not None:
            faiss.write_index(self.index, save_path)
            print(f"💾 FAISS index saved to {save_path}")
        else:
            print("⚠️ No index to save.")

    def load_index(self, path=None):
            load_path = path or self.index_path
            if os.path.exists(load_path):
                self.index = faiss.read_index(load_path)
                print(f"📂 FAISS index loaded from {load_path}")
            else:
                print(f"❌ Index file not found at {load_path}")

    def add_documents(self, texts):
        """
        Adds a list of documents to the advisor, embeds them, and updates the FAISS index.
        """
        if not texts:
            print("⚠️ No documents to add.")
            return

        print(f"📄 Adding {len(texts)} documents to index...")
        embeddings = self.model.encode(texts)
        self.index.add(embeddings)
        self.documents.extend(texts)
        print("✅ Documents embedded and indexed.")


