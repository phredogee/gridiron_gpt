# query_interface.py

from gridiron_gpt.pipeline import SemanticPipeline
from gridiron_gpt.app.notifier import notify_slack

def handle_query(user_query: str, top_n: int = 3):
    print(f"🔍 Received query: '{user_query}'")
    pipeline = SemanticPipeline()
    
    matches, index, embeddings = pipeline.run(query=user_query)
    
    if matches:
        top_matches = matches[:top_n]
        print("✅ Top semantic matches:")
        for i, match in enumerate(top_matches, 1):
            print(f"{i}. {match}")
        
        slack_message = (
            f"🏈 Semantic matches for '{user_query}':\n" +
            "\n".join([f"{i+1}. {m}" for i, m in enumerate(top_matches)])
        )
        notify_slack(slack_message)
    else:
        print(f"❌ No semantic match found for: '{user_query}'")
        notify_slack(f"😕 No semantic match found for '{user_query}'")
