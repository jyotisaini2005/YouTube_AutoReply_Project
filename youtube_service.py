from googleapiclient.discovery import build
from config import API_KEY
from auto_reply import get_reply
from save_data import save_comment, save_reply, save_video
import sqlite3

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


def fetch_comments(video_id):

    # ================= SAVE VIDEO DETAILS =================

    video_request = youtube.videos().list(
        part="snippet",
        id=video_id
    )

    video_response = video_request.execute()

    if video_response["items"]:

        video = video_response["items"][0]

        title = video["snippet"]["title"]
        channel = video["snippet"]["channelTitle"]
        published = video["snippet"]["publishedAt"]

        save_video(
            video_id,
            title,
            channel,
            published,
            "Direct Link"
        )

    # ================= FETCH COMMENTS =================

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=10,
        textFormat="plainText"
    )

    response = request.execute()

    conn = sqlite3.connect("youtube.db")
    cursor = conn.cursor()

    results = []

    for item in response["items"]:

        comment_id = item["id"]

        snippet = item["snippet"]["topLevelComment"]["snippet"]

        comment = snippet["textDisplay"]
        author = snippet["authorDisplayName"]
        timestamp = snippet["publishedAt"]

        # Check if comment already exists
        cursor.execute(
            "SELECT comment_id FROM comments WHERE comment_id=?",
            (comment_id,)
        )

        existing_comment = cursor.fetchone()

        if existing_comment is None:

            # Save comment
            save_comment(
                comment_id,
                video_id,
                author,
                comment,
                timestamp
            )

            # Generate reply
            reply = get_reply(comment)

            # Save reply
            save_reply(
                comment_id,
                reply,
                status="Pending"
            )

            results.append((comment, reply))

    conn.close()

    return results