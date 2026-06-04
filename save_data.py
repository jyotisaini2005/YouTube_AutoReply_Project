import sqlite3

conn = sqlite3.connect("youtube.db")

cursor = conn.cursor()

comment = "Great Video"
reply = "Thank you 😊"
video_id = "abc123"

cursor.execute(
    "INSERT INTO comments(comment, reply, video_id) VALUES (?, ?, ?)",
    (comment, reply, video_id)
)

conn.commit()

print("Data Saved Successfully!")

conn.close()