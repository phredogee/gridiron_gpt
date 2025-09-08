# gpt/phred/semantic/semantic.py
from gridiron_gpt.semantic.intake import FETCHERS, clean_player_data, save_player_data, embed_player_data

class SemanticPipeline:
    def __init__(self, source: str = "local"):
        self.source = source
        print(f"🚀 SemanticPipeline initialized with source={self.source!r}")

    def run(self):
        print("🔍 Running semantic analysis pipeline...")

        # Fetch
        if self.source not in FETCHERS:
            raise ValueError(f"Unknown source: {self.source}")
        raw_data = FETCHERS[self.source]()
        print(f"📦 Retrieved {len(raw_data)} player records")

        # Clean
        cleaned_data = clean_player_data(raw_data)
        print(f"🧹 Cleaned data: {len(cleaned_data)} records ready")

        # Embed
        embeddings = embed_player_data(cleaned_data)
        print(f"🧠 Generated embeddings for {len(embeddings)} records")

        # Store
        save_player_data(cleaned_data, embeddings)
        print("💾 Data and embeddings saved successfully")

        print("✅ Semantic analysis pipeline complete")
