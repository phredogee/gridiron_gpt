# config/settings.py

# Embedding model
EMBEDDING_MODEL_NAME = 'all-MiniLM-L6-v2'

# FAISS index settings
EMBEDDING_DIM = 384  # Depends on model used

# Advisor settings
DEFAULT_TOP_K = 5

# CLI settings
WELCOME_MESSAGE = "🏈 Welcome to GridironGPT — your fantasy football advisor!"
EXIT_COMMAND = "exit"
