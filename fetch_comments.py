from googleapiclient.discovery import build
from config import API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

video_id = input("Enter Video ID: ")

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=10,
    textFormat="plainText"
)

response = request.execute()

print("\nComments:\n")

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    print(comment)
    print("-" * 50)