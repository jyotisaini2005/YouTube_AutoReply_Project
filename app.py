import streamlit as st
import sqlite3
from youtube_service import fetch_comments
from export_csv import export_comments


st.set_page_config(
    page_title="YouTube Auto Reply System",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Auto Reply System")
st.markdown(
    "Fetch comments, generate replies, and manage history."
)

st.subheader("🔗 Enter YouTube Video Link")

link = st.text_input(
    "Paste YouTube Video Link"
)

video_id = ""

if "v=" in link:

    video_id = link.split(
        "v="
    )[1].split("&")[0]

    st.success(
        f"Video ID Extracted: {video_id}"
    )

elif "youtu.be/" in link:

    video_id = link.split(
        "youtu.be/"
    )[1].split("?")[0]

    st.success(
        f"Video ID Extracted: {video_id}"
    )

col1, col2 = st.columns(2)


# ================= FETCH COMMENTS =================

with col1:

    if st.button("Fetch Comments"):

        if video_id == "":

            st.error(
                "Please enter a valid YouTube link!"
            )

        else:

            comments = fetch_comments(
                video_id
            )

            st.success(
                "Comments fetched successfully!"
            )

            st.subheader(
                "Comments & Generated Replies"
            )

            for comment, reply in comments:

                st.write(
                    "💬 Comment:",
                    comment
                )

                st.write(
                    "🤖 Reply:",
                    reply
                )

                st.write(
                    "------------------------"
                )


# ================= SHOW HISTORY =================

with col2:

    if st.button("Show History"):

        if video_id == "":

            st.error(
                "Please enter a valid YouTube link!"
            )

        else:

            conn = sqlite3.connect(
                "youtube.db"
            )

            cursor = conn.cursor()

            # Analytics Dashboard

            cursor.execute(
                "SELECT COUNT(*) FROM videos"
            )

            total_videos = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM comments"
            )

            total_comments = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM replies"
            )

            total_replies = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM replies WHERE status='Pending'"
            )

            pending_replies = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM replies WHERE status='Posted'"
            )

            posted_replies = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM replies WHERE status='Failed'"
            )

            failed_replies = cursor.fetchone()[0]

            st.subheader(
                "📊 Analytics Dashboard"
            )

            st.write(
                "🎥 Total Videos Scanned:",
                total_videos
            )

            st.write(
                "💬 Total Comments Collected:",
                total_comments
            )

            st.write(
                "🤖 Total Replies Generated:",
                total_replies
            )

            st.write(
                "⏳ Pending Replies:",
                pending_replies
            )

            st.write(
                "✅ Posted Replies:",
                posted_replies
            )

            st.write(
                "❌ Failed Replies:",
                failed_replies
            )

            st.write(
                "-----------------------------------"
            )

            # Comment History

            cursor.execute("""
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
            WHERE comments.video_id=?
            """, (video_id,))

            rows = cursor.fetchall()

            if rows:

                st.subheader(
                    "📝 Comment History"
                )

                for row in rows:

                    st.write(
                        "🆔 Comment ID:",
                        row[0]
                    )

                    st.write(
                        "🎥 Video ID:",
                        row[1]
                    )

                    st.write(
                        "👤 Author:",
                        row[2]
                    )

                    st.write(
                        "💬 Comment:",
                        row[3]
                    )

                    st.write(
                        "🤖 Generated Reply:",
                        row[5]
                    )

                    st.write(
                        "📌 Status:",
                        row[6]
                    )

                    st.write(
                        "🕒 Time:",
                        row[4]
                    )

                    st.write(
                        "------------------------"
                    )

                # ================= CSV DOWNLOAD =================

                file_name = export_comments()

                with open(file_name, "rb") as file:

                    st.download_button(
                        label="📥 Download CSV",
                        data=file.read(),
                        file_name="comments_history.csv",
                        mime="text/csv"
                    )

            else:

                st.warning(
                    "No records found!"
                )

            conn.close()


st.write("-----------------------------------")

st.caption(
    "YouTube Auto Reply Project | Python + SQLite + Streamlit"
)