# ~/gridiron_gpt/phred_utils.py

from phred_utils import print_banner

def print_banner(title, emoji="🎯", width=40):
    pad = "═" * width
    print(f"\n{emoji} {title}\n{pad}")
