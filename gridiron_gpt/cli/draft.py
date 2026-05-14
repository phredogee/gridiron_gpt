# gridiron_gpt/cli/draft.py

import click
from gridiron_gpt.draft.config import LeagueConfig
from gridiron_gpt.draft.ranker import build_rankings, get_round_targets
from gridiron_gpt.feedback import banner, error


@click.group()
def draft():
    """🏆 Pre-season draft tools — rank, strategize, and build your board"""
    pass


@draft.command()
@click.option("--position", "-p", default=None, help="Filter by position (QB, RB, WR, TE, K, DEF)")
@click.option("--top", default=30, show_default=True, type=int, help="Number of players to show")
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--teams", default=12, show_default=True, type=int, help="League size")
@click.option("--rounds", default=15, show_default=True, type=int, help="Number of draft rounds")
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def rank(position, top, scoring, teams, rounds, changes_path):
    """📋 Rank players for the upcoming draft"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)
    try:
        df = build_rankings(config, changes_path=changes_path)
    except Exception as e:
        error(str(e))
        return

    if position:
        df = df[df["position"].str.upper() == position.upper()]
        if df.empty:
            banner(f"No players found for position: {position}", emoji="❓")
            return

    df = df.head(top)

    click.echo(f"\n🏆  Draft Rankings — {scoring.upper()}, {teams}-team\n")
    click.echo(f"  {'#':<4} {'Name':<26} {'Pos':<5} {'Team':<5} {'Hist':>6} {'ADP':>6} {'Score':>7}  Notes")
    click.echo("  " + "─" * 78)

    for _, row in df.iterrows():
        adp_str = f"{row['adp']:.1f}" if row["adp"] is not None else "—"
        note_parts = []
        if row.get("injury"):
            note_parts.append(f"[{row['injury']}]")
        if row.get("note"):
            note_parts.append(row["note"])
        if row.get("multiplier", 1.0) != 1.0:
            note_parts.append(f"×{row['multiplier']:.2f}")
        note = " ".join(note_parts)
        click.echo(
            f"  {int(row['rank']):<4} {row['name']:<26} {row['position']:<5} {row['team']:<5}"
            f" {row['hist_score']:>6.1f} {adp_str:>6} {row['composite']:>7.1f}  {note}"
        )
    click.echo()


@draft.command()
@click.option("--round", "round_num", required=True, type=int, help="Draft round number (1–15)")
@click.option("--teams", default=12, show_default=True, type=int)
@click.option("--rounds", default=15, show_default=True, type=int)
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def strategy(round_num, teams, rounds, scoring, changes_path):
    """🧠 Draft strategy and top targets for a specific round"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)
    targets, advice = get_round_targets(round_num, config)

    pick_start = (round_num - 1) * teams + 1
    pick_end = round_num * teams

    click.echo(f"\n🧠  Round {round_num} Strategy — {scoring.upper()}, {teams}-team\n")
    click.echo(f"  Picks:    #{pick_start}–#{pick_end}")
    click.echo(f"  Targets:  {', '.join(targets)}")
    click.echo(f"  Advice:   {advice}")

    try:
        df = build_rankings(config, changes_path=changes_path)
        available = df[
            (df["suggested_round"] == round_num) & (df["position"].isin(targets))
        ].head(5)

        if not available.empty:
            click.echo(f"\n  Top available in round {round_num}:")
            for _, row in available.iterrows():
                adp_str = f"ADP {row['adp']:.1f}" if row["adp"] is not None else "undrafted"
                click.echo(f"    #{int(row['rank']):<4} {row['name']:<25} {row['position']:<5} {adp_str}")
    except Exception:
        pass

    click.echo()


@draft.command()
@click.option("--scoring", default="ppr", show_default=True,
              type=click.Choice(["ppr", "half_ppr", "standard"]))
@click.option("--teams", default=12, show_default=True, type=int)
@click.option("--rounds", default=15, show_default=True, type=int)
@click.option("--top", default=200, show_default=True, type=int, help="Max players to show")
@click.option("--changes", "changes_path", default="data/offseason_changes.yaml",
              show_default=True, help="Path to offseason changes YAML")
def board(scoring, teams, rounds, top, changes_path):
    """📌 Full draft board grouped by suggested round"""
    config = LeagueConfig(teams=teams, rounds=rounds, scoring=scoring)

    try:
        df = build_rankings(config, changes_path=changes_path)
    except Exception as e:
        error(str(e))
        return

    df = df.head(top)

    banner(f"📌 Draft Board — {scoring.upper()}, {teams}-team, {rounds} rounds")
    click.echo(f"  Roster: {config.roster}")
    click.echo(f"  Lineup: {config.lineup}\n")

    current_round = 0
    for _, row in df.iterrows():
        r = int(row["suggested_round"])
        if r != current_round:
            current_round = r
            targets, advice = get_round_targets(current_round, config)
            click.echo(f"\n  ── Round {current_round}  (Target: {', '.join(targets)}) ──")
            click.echo(f"     {advice}\n")

        adp_str = f"ADP {row['adp']:.1f}" if row["adp"] is not None else "no ADP"
        note_parts = []
        if row.get("injury"):
            note_parts.append(f"[{row['injury']}]")
        if row.get("note"):
            note_parts.append(str(row["note"]))
        note = "  " + " ".join(note_parts) if note_parts else ""

        click.echo(
            f"  #{int(row['rank']):<4} {row['name']:<26} {row['position']:<5} {row['team']:<5}"
            f" {row['hist_score']:>6.1f}pts  {adp_str}{note}"
        )

    click.echo()
