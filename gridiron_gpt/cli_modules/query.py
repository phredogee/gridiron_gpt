import typer
from utils.semantic import semantic_query

def main(query: str, top: int = 5, provider: str = "mistral"):
    semantic_query(query, top_k=top, provider=provider)

if __name__ == "__main__":
    typer.run(main)
