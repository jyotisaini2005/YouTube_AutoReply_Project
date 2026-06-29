from googleapiclient.discovery import build
from config import API_KEY
from save_data import save_comment

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

video_id = input("Enter Video ID: ")

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=20,
    textFormat="plainText"
)

response = request.execute()

print("\n========== COMMENTS ==========\n")

for item in response["items"]:

    comment_id = item["id"]

    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

    author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

    time = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

    print(f"Author : {author}")
    print(f"Comment: {comment}")
    print("----------------------------")

    save_comment(
        comment_id,
        video_id,
        author,
        comment,
        time
    )

print("\n✅ Comments saved successfully.")