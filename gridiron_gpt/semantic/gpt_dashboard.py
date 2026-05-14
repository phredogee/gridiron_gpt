def query_gpt(prompt: str, dry_run: bool = False):
    if dry_run:
        print(f"🧪 Dry-run: Would query GPT with → {prompt}")
    else:
        response = call_gpt_api(prompt)
        print(f"🧠 GPT Response:\n{response}")
