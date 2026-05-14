# session_guards/check_gitignore.xsh

if not os.path.exists(".gitignore"):
    print("⚠️  Missing .gitignore — consider adding one for hygiene.")
else:
    print("✅ .gitignore found — session hygiene intact.")
