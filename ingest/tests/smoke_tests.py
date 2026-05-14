#!/usr/bin/env python3
import duckdb

con = duckdb.connect("/home/phredo/projects/my_project/ingest/duckdb/nfl.duckdb")

checks = {
    "Games per season":
        "SELECT season, COUNT(*) AS games FROM schedules GROUP BY season ORDER BY season;",
    "Weekly rows per season":
        "SELECT season, COUNT(*) AS rows FROM weekly GROUP BY season ORDER BY season;",
    "Top 10 target totals":
        """
        SELECT full_name, season, SUM(targets) AS tgt
        FROM weekly
        WHERE position IN ('WR','TE','RB')
        GROUP BY 1,2
        ORDER BY tgt DESC
        LIMIT 10;
        """
}
for title, sql in checks.items():
    print(f"\n=== {title} ===")
    print(con.sql(sql).df())

con.close()
