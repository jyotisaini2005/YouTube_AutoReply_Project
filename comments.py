from googleapiclient.discovery import build
from config import API_KEY
from auto_reply import get_reply
import sqlite3

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

video_id = input("Enter Video ID: ")

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=10
)

response = request.execute()

conn = sqlite3.connect("youtube.db")
cursor = conn.cursor()

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

    reply = get_reply(comment)

    cursor.execute(
        "INSERT INTO comments(comment, reply, video_id) VALUES (?, ?, ?)",
        (comment, reply, video_id)
    )

    print("Comment:", comment)
    print("Reply:", reply)
    print("----------------")

conn.commit()
conn.close()

print("All comments saved to database!")