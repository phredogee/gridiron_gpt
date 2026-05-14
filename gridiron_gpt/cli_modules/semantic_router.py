# cli/semantic_router.py

import spacy
from spacy.pipeline import EntityRuler
from typing import Optional
from dataclasses import dataclass

# ✅ Load base model
nlp = spacy.load("en_core_web_md")

# ✅ Add custom football patterns
ruler = EntityRuler(nlp, overwrite_ents=True)
patterns = [
    {"label": "POSITION", "pattern": [{"LOWER": "wr"}]},
    {"label": "POSITION", "pattern": [{"LOWER": "rb"}]},
    {"label": "POSITION", "pattern": [{"LOWER": "qb"}]},
    {"label": "POSITION", "pattern": [{"LOWER": "te"}]},
    {"label": "METRIC", "pattern": [{"LOWER": "targets"}]},
    {"label": "METRIC", "pattern": [{"LOWER": "yards"}]},
    {"label": "METRIC", "pattern": [{"LOWER": "touchdowns"}]},
    {"label": "METRIC", "pattern": [{"LOWER": "yac"}]},  # yards after catch
    {"label": "ZONE", "pattern": [{"LOWER": "red"}, {"LOWER": "zone"}]}
]
ruler.add_patterns(patterns)
nlp.add_pipe(ruler, before="ner")

# ✅ ParsedQuery dataclass
@dataclass
class ParsedQuery:
    domain: str
    position: Optional[str] = None
    metric: Optional[str] = None
    threshold: Optional[int] = None
    direction: Optional[str] = None
    sort_by: Optional[str] = None
    limit: Optional[int] = None
    raw_text: Optional[str] = None

# 🧠 Main parser function
def parse_query(text: str) -> ParsedQuery:
    doc = nlp(text.lower())

    position = None
    metric = None
    threshold = None
    direction = None
    sort_by = None
    limit = None

    # ✅ Extract entities
    for ent in doc.ents:
        if ent.label_ == "POSITION":
            position = ent.text.upper().rstrip("S")
        elif ent.label_ == "METRIC":
            metric = ent.text.lower()
            sort_by = metric

    # 🔍 Scan tokens for modifiers
    for token in doc:
        if token.like_num:
            threshold = int(token.text)
        elif token.text in {">", "above", "over"}:
            direction = "greater"
        elif token.text in {"<", "under", "below"}:
            direction = "less"
        elif token.text in {"top", "best"}:
            limit = 10

    return ParsedQuery(
        domain="nfl",
        position=position,
        metric=metric,
        threshold=threshold,
        direction=direction,
        sort_by=sort_by,
        limit=limit,
        raw_text=text
    )
