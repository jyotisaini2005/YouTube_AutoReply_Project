from googleapiclient.discovery import build
from config import API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

keyword = input("Enter keyword to search: ")

request = youtube.search().list(
    part="snippet",
    q=keyword,
    type="video",
    maxResults=5
)

response = request.execute()

for item in response["items"]:
    print("\nTitle:", item["snippet"]["title"])
    print("Video ID:", item["id"]["videoId"])
    print("----------------------")