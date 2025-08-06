# app/advisor.py

from project_gridiron_gpt.core.advisor import Advisor
import numpy as np

def build_advisor():
    return Advisor()

def debug_embedding():
    advisor = Advisor()
    text = "Justin Jefferson is expected to play"
    embedding = advisor.embed(text)
    print(f"🔍 Embedding debug for: {text}")
    print("Shape:", embedding.shape)
    print("Norm:", np.linalg.norm(embedding))
    print("Any NaNs?", np.isnan(embedding).any())
    print("Any Zeros?", np.all(embedding == 0))

# Uncomment to run manually
debug_embedding()