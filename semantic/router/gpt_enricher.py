# semantic/router/gpt_enricher.py

from semantic.ingestion.espn_ingest import get_player_stats
from semantic.feedback import banner_success, banner_warn

def enrich_prompt(player_name: str, context: str, dry_run: bool = False) -> str:
    stats = get_player_stats(player_name)
    
    if not stats:
        banner_warn(f"No ESPN data found for {player_name}")
        return context

    enriched = f"{context}\n\n📊 ESPN Stats for {player_name}:\n{stats}"

    if dry_run:
        banner_success("🧪 Dry-run: Prompt enriched but not sent to GPT")
        print(enriched)
        return enriched

    # Placeholder for GPT call
    # response = call_gpt_api(enriched)
    # return response

    banner_success("✅ Prompt enriched and ready for GPT")
    return enriched
