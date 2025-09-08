import spacy
from spacy.pipeline import EntityRuler

def load_nlp():
    nlp = spacy.load("en_core_web_md")
    ruler = EntityRuler(nlp, overwrite_ents=True)

    patterns = [
        {"label": "POSITION", "pattern": [{"LOWER": "wr"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "rb"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "qb"}]},
        {"label": "POSITION", "pattern": [{"LOWER": "te"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "targets"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "yards"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "touchdowns"}]},
        {"label": "METRIC", "pattern": [{"LOWER": "yac"}]},
        {"label": "ZONE", "pattern": [{"LOWER": "red"}, {"LOWER": "zone"}]}
    ]

    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler, before="ner")
    return nlp
