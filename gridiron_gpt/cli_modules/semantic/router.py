# semantic/router.py

from semantic.parser import nlp
from cli.rushing import run_rushing_query
from cli.receiving import run_receiving_query

def route_query(text: str):
    doc = nlp(text)
    print(f"🧠 Interpreting query: '{text}'")

    for ent in doc.ents:
        print(f"🔍 Found entity: {ent.text} ({ent.label_})")

    if "rushing" in text.lower():
        player = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), None)
        if player:
            print(f"🏈 Player: {player}")
            run_rushing_query(player=player)
        else:
            print("⚠️ No player found in query.")

    elif "receiving" in text.lower():
        player = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), None)
        if player:
            print(f"🏈 Player: {player}")
            run_receiving_query(player=player)
        else:
            print("⚠️ No player found in query.")

    else:
        print("🤷 Query type not recognized.")
