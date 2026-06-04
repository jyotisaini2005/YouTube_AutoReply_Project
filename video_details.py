from googleapiclient.discovery import build
from config import API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

video_id = input("Enter Video ID: ")

request = youtube.videos().list(
    part="snippet,statistics",
    id=video_id
)

response = request.execute()

video = response["items"][0]

print("\nVideo Details")
print("---------------------")
print("Title:", video["snippet"]["title"])
print("Channel Name:", video["snippet"]["channelTitle"])
print("Views:", video["statistics"].get("viewCount", "N/A"))
print("Likes:", video["statistics"].get("likeCount", "N/A"))
print("Publish Date:", video["snippet"]["publishedAt"])