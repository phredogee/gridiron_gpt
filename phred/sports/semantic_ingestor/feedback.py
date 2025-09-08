# semantic_ingestor/feedback.py

def banner_success(message: str):
    print(f"\n✅ SUCCESS: {message}\n")

def banner_error(message: str):
    print(f"\n❌ ERROR: {message}\n")

def banner_hint(message: str):
    print(f"\n💡 HINT: {message}\n")

def banner_info(message: str):
    print(f"\n📘 INFO: {message}\n")

def banner_warning(message: str):
    print(f"\n⚠️ WARNING: {message}\n")
