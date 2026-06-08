from googleapiclient.discovery import build
from textblob import TextBlob
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
    maxResults=100
)

response = request.execute()

total_comments = 0
positive_comments = 0
negative_comments = 0

for item in response["items"]:

    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

    polarity = TextBlob(comment).sentiment.polarity

    total_comments += 1

    if polarity > 0:
        positive_comments += 1
    elif polarity < 0:
        negative_comments += 1
print("\nComment Analysis")
print("----------------------")
print("Total Comments:", total_comments)
print("Positive Comments:", positive_comments)
print("Negative Comments:", negative_comments)