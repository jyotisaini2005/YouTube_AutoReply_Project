import sqlite3
import pandas as pd

conn = sqlite3.connect("youtube.db")

query = "SELECT * FROM comments"

df = pd.read_sql_query(query, conn)

df.to_csv("comments_history.csv", index=False)

print("CSV File Created Successfully!")

conn.close()