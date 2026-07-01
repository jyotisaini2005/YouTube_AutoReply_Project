import sqlite3
import pandas as pd


def export_comments():

    conn = sqlite3.connect("youtube.db")

    query = """
    SELECT
        comments.comment_id,
        comments.video_id,
        comments.author,
        comments.comment,
        comments.timestamp,
        replies.reply_text,
        replies.status
    FROM comments
    LEFT JOIN replies
    ON comments.comment_id = replies.comment_id
    """

    df = pd.read_sql_query(query, conn)

    df.to_csv(
        "comments_history.csv",
        index=False
    )

    conn.close()

    return "comments_history.csv"


if __name__ == "__main__":

    file = export_comments()

    print(f"{file} created successfully!")