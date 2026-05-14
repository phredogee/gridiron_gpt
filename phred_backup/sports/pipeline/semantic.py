# phred/sports/pipeline/semantic.py

def run_semantic_pipeline(players: list[dict], dry_run: bool = True) -> dict:
    from phred.sports.fetchers.espn.bios import get_player_bios
    from phred.semantic.embed import embed_texts  # Assuming this exists

    bios = get_player_bios()
    if not bios:
        print("📭 No bios found. Skipping embedding and audit.")
        return {}

    embeddings = embed_texts(bios, mode="stub" if dry_run else "live")
    print(f"✅ Embedded {len(bios)} bios using mode: {'stub' if dry_run else 'live'}")

    issues = audit_embeddings(bios, embeddings)
    if issues:
        print("🔍 Semantic Audit Issues:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("🎯 All embeddings passed audit checks.")

    # Optional: check for missing metadata
    missing = [p["name"] for p in players if p["name"] not in [b["name"] for b in bios]]
    if missing:
        print(f"⚠️ Missing metadata for {len(missing)} players:")
        for name in missing:
            print(f"   - {name}")

    return embeddings

def embed_texts(texts, mode="stub"):
    results = []
    for text in texts:
        if mode == "stub":
            vec = [0.1] * 768
            confidence = 0.3 if not text.strip() else 0.9
        elif mode == "live":
            # Replace with actual embedding call
            vec = embed_live(text)
            confidence = compute_confidence(vec)  # heuristic or model-based
        else:
            raise ValueError(f"Unknown embedding mode: {mode}")
        results.append({"embedding": vec, "confidence": confidence})
    return results

def audit_embeddings(bios, embeddings):
    issues = []
    for i, (bio, emb) in enumerate(zip(bios, embeddings)):
        tags = []
        if not bio.strip():
            tags.append("empty_bio")
        if not emb["embedding"] or len(emb["embedding"]) != 768:
            tags.append("invalid_vector")
        elif emb["confidence"] < 0.5:
            tags.append("low_confidence")
        if tags:
            issues.append({
                "index": i,
                "name": bio[:30],  # preview
                "tags": tags,
                "confidence": emb["confidence"]
            })
    return issues

def run_semantic_pipeline(players: list[dict], dry_run: bool = True) -> list[dict]:
    bios = get_player_bios()
    embeddings = embed_texts(bios, mode="stub" if dry_run else "live")
    results = []

    for player, emb in zip(players, embeddings):
        results.append({
            "name": player["name"],
            "bio": player.get("bio", ""),
            "embedding": emb["embedding"],
            "confidence": emb["confidence"]
        })

    return results

if __name__ == "__main__":
    import argparse
    from pipeline.intake import get_player_bios  # or wherever bios live

    parser = argparse.ArgumentParser(description="Semantic embedding pipeline")
    parser.add_argument("--mode", choices=["stub", "live"], default="stub", help="Embedding mode")
    parser.add_argument("--audit", action="store_true", help="Run semantic audit")
    parser.add_argument("--audit-semantic", action="store_true", help="Run semantic audit with tags and confidence")
    args = parser.parse_args()

    bios = get_player_bios()
    embeddings = embed_texts(bios, mode=args.mode)

    print(f"✅ Embedded {len(bios)} bios using mode: {args.mode}")
    
    if args.audit:
        issues = audit_embeddings(bios, embeddings)
        if issues:
            print("🔍 Semantic Audit Issues:")
            for issue in issues:
                print(f"  {issue}")
        else:
            print("🎯 All embeddings passed audit checks.")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-semantic", action="store_true")
    args = parser.parse_args()

    if args.audit_semantic:
        print("🔍 Auditing semantic pipeline...")
        # Run audit logic here

if __name__ == "__main__":
    main()
