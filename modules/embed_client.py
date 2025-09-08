import os
from mistralai.client import MistralClient
from openai import OpenAI

class EmbedClient:
    def __init__(self, provider="mistral", model=None):
        self.provider = provider.lower()
        self.model = model or self._default_model()
        self.client = self._init_client()

    def _default_model(self):
        return {
            "mistral": "mistral-embed",
            "openai": "text-embedding-ada-002"
        }.get(self.provider, "mistral-embed")

    def _init_client(self):
        if self.provider == "mistral":
            return MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))
        elif self.provider == "openai":
            return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def embed(self, text):
        if isinstance(text, dict):
            text = ", ".join(f"{k}={v}" for k, v in text.items())
        elif not isinstance(text, str):
            text = str(text)

        if self.provider == "mistral":
            response = self.client.embeddings(model=self.model, input=[text])
            return response.data[0].embedding
        elif self.provider == "openai":
            response = self.client.embeddings.create(model=self.model, input=[text])
            return response.data[0].embedding
