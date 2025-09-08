# phredenv/banner.py

def show_banner():
    if __xonsh__.env.get("PHRED_DEBUG"):
        print("🚀 [phredenv] Debug mode enabled")
    print("🎩 phredenv loaded successfully.")
