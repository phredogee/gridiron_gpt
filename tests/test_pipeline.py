from gridiron_gpt.core.advisor import Advisor
from pipelines.ranking_pipeline import run_pipeline_logic

advisor = Advisor()

print("Advisor class:", advisor.__class__)
print("Advisor method args:", advisor.add_documents.__code__.co_varnames)
print("Method:", advisor.add_documents)
print("Method type:", type(advisor.add_documents))

run_pipeline_logic("ranking", advisor=advisor)
