import sqlite3

conn = sqlite3.connect("youtube.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT,
    reply TEXT,
    sentiment TEXT,
    video_id TEXT
)
""")

conn.commit()

print("Database Created Successfully!")

conn.close()