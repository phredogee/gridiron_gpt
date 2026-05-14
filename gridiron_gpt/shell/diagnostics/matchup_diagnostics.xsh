# projects/gridiron_gpt/shell/diagnostics/matchup_diagnostics.py

import pandas as pd
import os
from datetime import datetime

def pick_seasonal_emoji():
    month = datetime.now().month
    day = datetime.now().day
    if month == 10 and day >= 15:
        return "🎃"
    elif month in [9, 10, 11]:
        return "🍂"
    else:
        return "🌟"

def run_diagnostics():
    weekly_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/data/weekly_stats.csv")
    print(f"📂 Reading data from: {weekly_path}")

    if not os.path.exists(weekly_path):
        print("❌ weekly_stats.csv not found.")
        print("🧊 No data? No worries. Your shell still believes in you 💫")
        return

    if os.path.getsize(weekly_path) == 0:
        print("⚠️ weekly_stats.csv is empty. No matchup diagnostics available.")
        print("🧊 Even empty files deserve a second chance. You’ve got this 🧡")
        return

    try:
        df = pd.read_csv(weekly_path, nrows=5000)
        df = df.dropna(subset=['fantasy_points'])
        df['fantasy_points'] = pd.to_numeric(df['fantasy_points'], errors='coerce')
        df = df.drop_duplicates(subset=['player_id', 'season', 'week'])

        df['date'] = pd.to_datetime(
            df['season'].astype(str) + 'W' + df['week'].astype(str) + '-1',
            format='%YW%W-%w',
            errors='coerce'
        )

        cleaned_path = os.path.expanduser("~/projects/my_project/gridiron_gpt/data/weekly_stats_cleaned.csv")
        df.to_csv(cleaned_path, index=False)
        print(f"🧼 Cleaned data saved to: {cleaned_path}")
        print("📊 Data loaded. Running matchup diagnostics...")

        columns = df.columns.str.lower()
        team_col = next((col for col in columns if 'team' in col and 'recent' in col), None)
        opp_col = next((col for col in columns if 'opponent' in col), None)
        points_col = next((col for col in columns if 'fantasy_points' in col and 'ppr' not in col), None)

        if not all([team_col, opp_col, points_col]):
            print("⚠️ Required columns not found. Skipping diagnostics.")
            print("🧊 Your shell still believes in you. Columns are quirky, but so are contributors 💫")
            return

        df_matchups = df.groupby([team_col, opp_col]).agg({points_col: 'sum'}).reset_index()
        df_matchups = df_matchups.sort_values(points_col, ascending=False).head(5)

        print("🧠 Top 5 Fantasy Matchups — Week 5")
        for i, row in df_matchups.iterrows():
            print(f"{i+1}. {row[team_col]} vs. {row[opp_col]} — {row[points_col]:.1f} pts")

        emoji = pick_seasonal_emoji()
        print(f"{emoji} Diagnostics complete. Your shell is proud of you.")

    except Exception as e:
        print(f"💥 Error during diagnostics: {e}")
        print("🧊 Something broke, but not your spirit. Keep going 💪")
