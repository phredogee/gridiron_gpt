# /cli/nlp_setup.py

import spacy
from spacy.pipeline import EntityRuler

def build_nlp():
    print("🔧 Initializing spaCy pipeline...")
    nlp = spacy.load("en_core_web_sm")

    # ✅ Add EntityRuler via registered name
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    patterns = [
        {"label": "STAT", "pattern": "receptions"},
        {"label": "STAT", "pattern": "targets"},
        {"label": "ZONE", "pattern": "end zone"},
]
ruler.add_patterns(patterns)

    print("📌 EntityRuler added before NER")

    # 🧠 Add custom patterns
    ruler.add_patterns([
        {"label": "POSITION", "pattern": "wide receiver"},
        {"label": "STAT", "pattern": [{"LOWER": "catches"}, {"IS_DIGIT": True}]},
        {"label": "STAT", "pattern": [{"IS_DIGIT": True}, {"LOWER": "catches"}]},
        {"label": "STAT", "pattern": [{"TEXT": ">"}, {"IS_DIGIT": True}, {"LOWER": "catches"}]},
        {"label": "STAT", "pattern": [{"LIKE_NUM": True}, {"LOWER": "catches"}]},
        {"label": "ZONE", "pattern": "red zone"},
    ])
    print("✨ Custom patterns loaded into EntityRuler")

    return nlp

    patterns = [
        # Positions
        {"label": "POSITION", "pattern": [{"LOWER": "wr"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "rb"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "qb"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "te"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "wide"}, {"LOWER": "receiver"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "running"}, {"LOWER": "back"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "tight"}, {"LOWER": "end"}]},

        # Metrics
        {"label": "METRIC", "pattern": [{"LOWER": "targets"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "receptions"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "catches"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "touchdowns"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "tds"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "interceptions"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "picks"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "completions"}]},

        # Zones
        {"label": "ZONE", "pattern": [{"LOWER": "red"}, {"LOWER": "zone"}]},
        {"label": "ZONE", "pattern": [{"LOWER": "end"}, {"LOWER": "zone"}]},
        {"label": "ZONE", "pattern": [{"LOWER": "goal"}, {"LOWER": "line"}]},
    ]

    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler, before="ner")
    return nlp
