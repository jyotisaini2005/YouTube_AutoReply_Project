from googleapiclient.discovery import build
from config import API_KEY
from save_data import save_keyword, save_video

# YouTube API
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

# User Input
keyword = input("Enter keyword to search: ")

# Save searched keyword
save_keyword(keyword)

# Search Videos
request = youtube.search().list(
    part="snippet",
    q=keyword,
    type="video",
    maxResults=10,
    order="relevance"
)

response = request.execute()

print("\n=========== Videos Found ===========\n")

for item in response["items"]:

    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    published = item["snippet"]["publishedAt"]

    print(f"Title      : {title}")
    print(f"Video ID   : {video_id}")
    print(f"Channel    : {channel}")
    print(f"Published  : {published}")
    print("-------------------------------------------")

    # Save Video in Database
    save_video(
        video_id,
        title,
        channel,
        published,
        keyword
    )

print("\n✅ All videos saved into database successfully.")