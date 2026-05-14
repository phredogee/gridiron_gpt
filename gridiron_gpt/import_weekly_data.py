# ~/projects/my_project/gridiron_gpt/import_weekly_data.py

import nfl_data_py as nfl
import pandas as pd

print("📦 Importing weekly NFL fantasy data...")
df = nfl.import_weekly_data(years=[2023, 2024])
df.to_csv("data/weekly_stats.csv", index=False)
print("✅ Data saved to weekly_stats.csv")
