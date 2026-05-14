# gridiron_gpt/core/llm.py

import os
from typing import Optional

_DEFAULT_MODEL = "claude-haiku-4-5-20251001"

SYSTEM_PROMPT = """You are a sharp fantasy football advisor. You have access to real player stats.

Rules:
- Answer using ONLY the player data provided — do not invent stats
- Be specific: name players, cite points, mention team/position
- Give a clear top recommendation with 1-2 sentences of reasoning
- If injury or surface notes are relevant to the question, mention them
- Keep it tight — no fluff, no disclaimers"""


def generate_advice(
    query: str,
    context_docs: list,
    model: str = _DEFAULT_MODEL,
) -> Optional[str]:
    """
    Call Claude to generate fantasy advice from retrieved player docs.
    Returns None if ANTHROPIC_API_KEY is not set.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

        context = "\n".join(f"- {doc['text']}" for doc in context_docs)

        message = client.messages.create(
            model=model,
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": f"Question: {query}\n\nPlayer data:\n{context}",
            }],
        )
        return message.content[0].text

    except Exception as e:
        return f"[LLM error: {e}]"
