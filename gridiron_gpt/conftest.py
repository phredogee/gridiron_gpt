try:
    import requests
    print("✅ requests is importable from test context.")
except ImportError:
    print("❌ requests is still missing in test context.")
# try:
#     from phred.slack_bot import SlackBot
#     print("✅ SlackBot import succeeded.")
# except ImportError as e:
#     print(f"❌ SlackBot import failed: {e}")
