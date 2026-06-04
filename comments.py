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
    maxResults=10
)

response = request.execute()

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    print(comment)
    print("----------------")