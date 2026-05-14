#!/usr/bin/env python3
from __future__ import annotations
import os, sys, math, datetime as dt
from pathlib import Path
from glob import glob
import pandas as pd
import duckdb
import typer
from rich import print as rprint
import nfl_data_py as nfl

app = typer.Typer(help="NFL open data ingestion → Parquet → DuckDB")

# ---------- Utils ----------
def seasons_range(start:int, end:int)->list[int]:
    if end < start: raise ValueError("end season < start season")
    return list(range(start, end+1))

def ensure_dir(p:Path):
    p.mkdir(parents=True, exist_ok=True)

def write_parquet(df: pd.DataFrame, path: Path):
    ensure_dir(path.parent)
    df.to_parquet(path, index=False)

def write_partitioned(df: pd.DataFrame, base: Path, season_col="season"):
    ensure_dir(base)
    for yr, chunk in df.groupby(season_col, dropna=False):
        if pd.isna(yr): continue
        path = base / f"season={int(yr)}" / f"{base.name}_{int(yr)}.parquet"
        ensure_dir(path.parent)
        chunk.to_parquet(path, index=False)

def connect_duck(path: Path):
    ensure_dir(path.parent)
    return duckdb.connect(str(path))

def parquet_glob(base: Path, pattern: str):
    return str(base / pattern)

def load_cfg():
    import tomllib
    with open(Path(__file__).with_name("config.toml"), "rb") as f:
        return tomllib.load(f)

# ---------- Ingest steps ----------
def import_schedules(seasons:list[int])->pd.DataFrame:
    return nfl.import_schedules(seasons)

def import_rosters(seasons: list[int]) -> pd.DataFrame:
    """
    Load roster-like data across seasons. Tries canonical, then weekly, then seasonal.
    Normalizes to a single DataFrame so the rest of the pipeline doesn't care.
    """
    # Try canonical name first
    if hasattr(nfl, "import_rosters"):
        return nfl.import_rosters(seasons)

    # Weekly rosters (preferred when canonical missing)
    if hasattr(nfl, "import_weekly_rosters"):
        dfs = []
        for yr in seasons:
            df = nfl.import_weekly_rosters([yr])
            # ensure a 'season' column exists for partitioning
            if "season" not in df.columns:
                df["season"] = yr
            dfs.append(df)
        return pd.concat(dfs, ignore_index=True)

    # Seasonal rosters (coarser grain)
    if hasattr(nfl, "import_seasonal_rosters"):
        dfs = []
        for yr in seasons:
            df = nfl.import_seasonal_rosters([yr])
            if "season" not in df.columns:
                df["season"] = yr
            dfs.append(df)
        return pd.concat(dfs, ignore_index=True)

    # Last resort: derive a minimal roster from players table
    rprint("[yellow]Warning:[/yellow] roster function not found; using players() fallback")
    players = import_players()
    keep = [c for c in players.columns if c in {
        "player_id","gsis_id","nfl_id","pfr_id","pff_id","espn_id","sportradar_id",
        "full_name","position","team","status","birth_date","height","weight"
    }]
    # copy and synthesize a 'season' column so partitioning still works
    out = players[keep].copy()
    out["season"] = max(seasons)  # place in latest season by default
    return out

def _concat_ok(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def import_weekly(seasons: list[int]) -> pd.DataFrame:
    dfs = []
    for yr in seasons:
        try:
            df = nfl.import_weekly_data([yr])
            if "season" not in df.columns:
                df["season"] = yr
            dfs.append(df)
            rprint(f"[cyan]✓ weekly {yr}[/cyan]")
        except Exception as e:
            rprint(f"[yellow]↷ skipping weekly {yr} ({e.__class__.__name__}: {e})[/yellow]")
    return _concat_ok(dfs)

def import_season(seasons: list[int]) -> pd.DataFrame:
    dfs = []
    for yr in seasons:
        try:
            df = nfl.import_seasonal_data([yr])
            if "season" not in df.columns:
                df["season"] = yr
            dfs.append(df)
            rprint(f"[cyan]✓ season {yr}[/cyan]")
        except Exception as e:
            rprint(f"[yellow]↷ skipping season {yr} ({e.__class__.__name__}: {e})[/yellow]")
    return _concat_ok(dfs)

def import_pbp(seasons: list[int]) -> pd.DataFrame:
    dfs = []
    for yr in seasons:
        try:
            rprint(f"[cyan]→ loading PBP {yr}[/cyan]")
            dfs.append(nfl.import_pbp_data([yr]))
            rprint(f"[cyan]✓ pbp {yr}[/cyan]")
        except Exception as e:
            rprint(f"[yellow]↷ skipping pbp {yr} ({e.__class__.__name__}: {e})[/yellow]")
    return _concat_ok(dfs)

def import_players()->pd.DataFrame:
    return nfl.import_players()

def import_ids()->pd.DataFrame:
    return nfl.import_ids()

# ---------- Commands ----------
@app.command()
def bootstrap():
    """
    One-time historical pull → Parquet, then create DuckDB views.
    """
    cfg = load_cfg()
    seasons = seasons_range(cfg["bootstrap_start_season"], cfg["bootstrap_end_season"])
    base = Path(cfg["data_parquet_dir"])
    rprint(f"[bold]Bootstrapping seasons {seasons[0]}–{seasons[-1]}[/bold]")

    tbl = cfg["tables"]

    if tbl["schedules"]:
        schedules = import_schedules(seasons)
        write_partitioned(schedules, base / "schedules")

    if tbl["rosters"]:
        rosters = import_rosters(seasons)
        write_partitioned(rosters, base / "rosters")

    if tbl["weekly"]:
        weekly = import_weekly(seasons)
        write_partitioned(weekly, base / "weekly")

    if tbl["season"]:
        season = import_season(seasons)
        write_partitioned(season, base / "season")

    if tbl["pbp"]:
        pbp = import_pbp(seasons)
        write_partitioned(pbp, base / "pbp", season_col="season")

    if tbl["players"]:
        players = import_players()
        write_parquet(players, base / "players" / "players.parquet")

    if tbl["ids"]:
        ids = import_ids()
        write_parquet(ids, base / "ids" / "ids.parquet")

    build_duck_views()
    rprint("[green]Bootstrap complete.[/green]")

from glob import glob

@app.command()
def build_duck_views():
    """
    (Re)create convenient DuckDB views over Parquet partitions.
    Skips any view whose source pattern has no files yet.
    """
    cfg = load_cfg()
    base = Path(cfg["data_parquet_dir"]).resolve()
    con = connect_duck(Path(cfg["duckdb_path"]))

    def mkview(name: str, folder: str, wildcard: str):
        # Build a glob pattern like data/nfl/parquet/weekly/*.parquet
        src = parquet_glob(base / folder, wildcard)
        # If nothing matches, skip to avoid DuckDB "No files found" exception
        if not glob(src):
            rprint(f"[yellow]↷ skipping view {name} — no files at {src}[/yellow]")
            return
        con.sql(f"CREATE OR REPLACE VIEW {name} AS SELECT * FROM read_parquet('{src}');")
        rprint(f"[green]✓ view {name}[/green]")

    # Partitioned season dirs
    if (base / "pbp").exists():
        mkview("pbp", "pbp", "season=*/pbp_*.parquet")
    if (base / "weekly").exists():
        mkview("weekly", "weekly", "season=*/weekly_*.parquet")  # may be single or split files
    if (base / "season").exists():
        mkview("season", "season", "season=*/season_*.parquet")
    if (base / "schedules").exists():
        mkview("schedules", "schedules", "season=*/schedules_*.parquet")
    if (base / "rosters").exists():
        mkview("rosters", "rosters", "season=*/rosters_*.parquet")

    # Single-file views
    players_path = base / "players" / "players.parquet"
    if players_path.exists():
        con.sql(f"CREATE OR REPLACE VIEW players AS SELECT * FROM read_parquet('{players_path.as_posix()}');")
        rprint("[green]✓ view players[/green]")
    else:
        rprint(f"[yellow]↷ skipping view players — no file at {players_path}[/yellow]")

    ids_path = base / "ids" / "ids.parquet"
    if ids_path.exists():
        con.sql(f"CREATE OR REPLACE VIEW ids AS SELECT * FROM read_parquet('{ids_path.as_posix()}');")
        rprint("[green]✓ view ids[/green]")
    else:
        rprint(f"[yellow]↷ skipping view ids — no file at {ids_path}[/yellow]")

    con.close()
    rprint("[green]DuckDB views rebuilt.[/green]")

@app.command()
def update_recent(days:int|None=None):
    """
    Re-pull recent windows to catch corrections. Defaults to config.recent_days.
    """
    cfg = load_cfg()
    days = days or int(cfg["recent_days"])
    today = dt.date.today()
    # Approx seasons touched: current and maybe previous
    current_year = today.year
    seasons = list({current_year, current_year-1})
    rprint(f"[bold]Refreshing last {days} days → seasons {sorted(seasons)}[/bold]")

    base = Path(cfg["data_parquet_dir"])
    tbl = cfg["tables"]

    # schedules + weekly + pbp tend to change post-game
    if tbl["schedules"]:
        write_partitioned(import_schedules(list(seasons)), base / "schedules")
    if tbl["weekly"]:
        write_partitioned(import_weekly(list(seasons)), base / "weekly")
    if tbl["pbp"]:
        write_partitioned(import_pbp(list(seasons)), base / "pbp", season_col="season")
    if tbl["rosters"]:
        write_partitioned(import_rosters(list(seasons)), base / "rosters")

    build_duck_views()
    rprint("[green]Recent update complete.[/green]")

@app.command()
def sanity():
    """
    Quick row counts to verify the pipeline is alive.
    """
    cfg = load_cfg()
    con = connect_duck(Path(cfg["duckdb_path"]))
    for view in ["schedules","weekly","season","pbp","rosters","players","ids"]:
        try:
            cnt = con.sql(f"SELECT COUNT(*) FROM {view}").fetchone()[0]
            rprint(f"[cyan]{view}[/cyan]: {cnt:,} rows")
        except Exception as e:
            rprint(f"[yellow]{view}[/yellow]: (not present) {e}")
    con.close()

if __name__ == "__main__":
    app()
