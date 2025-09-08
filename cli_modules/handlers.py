# /cli/hamdlers.py

import pandas as pd

def load_nfl_data():
    # Replace with nflverse or local CSV
    return pd.read_csv("data/nfl_stats.csv")

def get_targets(position, threshold, direction, limit):
    df = load_nfl_data()
    df = df[df["position"] == position]

    if direction == "greater":
        df = df[df["targets"] > threshold]
    elif direction == "less":
        df = df[df["targets"] < threshold]

    df = df.sort_values("targets", ascending=False).head(limit)
    return df[["player", "team", "targets"]]

def get_touchdowns(position, threshold, direction, limit):
    df = load_nfl_data()
    df = df[df["position"] == position]

    if direction == "greater":
        df = df[df["touchdowns"] > threshold]
    elif direction == "less":
        df = df[df["touchdowns"] < threshold]

    df = df.sort_values("touchdowns", ascending=False).head(limit)
    return df[["player", "team", "touchdowns"]]
