import duckdb
con = duckdb.connect("duckdb/nfl.duckdb")
print(con.sql("SELECT season, COUNT(*) AS games FROM schedules GROUP BY season ORDER BY season;").df())
con.close()
