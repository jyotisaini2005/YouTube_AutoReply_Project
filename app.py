import streamlit as st
import sqlite3
from youtube_service import fetch_comments

st.set_page_config(
    page_title="YouTube Auto Reply System",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Auto Reply System")
st.markdown("Fetch comments, generate replies, and manage history.")

st.subheader("🔗 Enter YouTube Video Link")

link = st.text_input("Paste YouTube Video Link")

video_id = ""

if "v=" in link:
    video_id = link.split("v=")[1].split("&")[0]
    st.success(f"Video ID Extracted: {video_id}")

elif "youtu.be/" in link:
    video_id = link.split("youtu.be/")[1].split("?")[0]
    st.success(f"Video ID Extracted: {video_id}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Fetch Comments"):

        if video_id == "":
            st.error("Please enter a valid YouTube link!")

        else:
            comments = fetch_comments(video_id)

            st.success("Comments fetched successfully!")

            st.subheader("Comments & Replies")

            for comment, reply in comments:
                st.write("Comment:", comment)
                st.write("Reply:", reply)
                st.write("------------------------")
with col2:
    if st.button("Show History"):

        if video_id == "":
            st.error("Please enter a valid YouTube link!")

        else:

            conn = sqlite3.connect("youtube.db")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM comments WHERE video_id=?",
                (video_id,)
            )

            rows = cursor.fetchall()

            if rows:

                st.subheader("Comment Statistics")

                total_comments = len(rows)
                custom_replies = 0
                default_replies = 0

                for row in rows:

                    if row[2] == "Thank you for your comment 😊":
                        default_replies += 1
                    else:
                        custom_replies += 1

                st.write("Total Comments:", total_comments)
                st.write("Custom Replies:", custom_replies)
                st.write("Default Replies:", default_replies)

                st.write("-----------------------------------")
                st.subheader("Comment History")

                for row in rows:

                    st.write("ID:", row[0])
                    st.write("Comment:", row[1])
                    st.write("Reply:", row[2])
                    st.write("Video ID:", row[3])

                    st.write("------------------------")

            else:
                st.warning("No records found!")

            conn.close()

st.write("-----------------------------------")
st.caption("YouTube Auto Reply Project | Python + SQLite + Streamlit")