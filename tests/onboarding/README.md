# 🧭 Onboarding Walkthroughs for gridiron_gpt

Welcome, contributor! This folder contains guided test modules designed to help you understand how query logic works inside `gridiron_gpt`.

## 🧪 What's Inside

- `test_query_walkthrough.py`: A step-by-step tutorial on writing safe, expressive query tests.
- Emoji-tiered feedback to help you spot wins and failures at a glance.
- Examples of error handling, parametrized tests, and assertion clarity.

## 🚀 How to Run

From the project root:

```bash
pytest tests/onboarding/ --maxfail=5 -v

## 🧪 Activation Walkthrough

- `test_activation_walkthrough.py`: Validates virtualenv state, shell context, and activation quirks.
- Helps contributors detect mismatches and fix them with expressive feedback.
