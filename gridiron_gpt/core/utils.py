# core/utils.py
import faiss

def save_index(index, path):
    print(f"💾 Saving index to: {path}")
    faiss.write_index(index, path)

def load_index_from_file(path):
    print(f"📥 Loading index from: {path}")
    return faiss.read_index(path)

def load_documents_from_file(path):
    print(f"📂 Reading documents from: {path}")
    with open(path, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f if line.strip()]
    return documents

from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_documents(documents):
    print(f"🔢 Embedding {len(documents)} documents...")
    return _model.encode(documents, normalize_embeddings=True)