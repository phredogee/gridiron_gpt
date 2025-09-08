# /modules/semantic_query.py

import spacy
nlp = spacy.load("en_core_web_sm")

def parse_query(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    metric = next((token.text for token in doc if token.text in ["snap share", "red zone touches", "target share"]), None)
    intent = "compare" if "compare" in text else "lookup"
    return {"entities": entities, "metric": metric, "intent": intent}
