import sqlite3

conn = sqlite3.connect("youtube.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM comments")
rows = cursor.fetchall()

for row in rows:
    print("ID:", row[0])
    print("Comment:", row[1])
    print("Reply:", row[2])
    print("Video ID:", row[3])
    print("--------------------------------")

conn.close()