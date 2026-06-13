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

# Input Section
st.subheader("🔗 Enter YouTube Video Link")

link = st.text_input("Paste YouTube Video Link")

video_id = ""

if "v=" in link:
    video_id = link.split("v=")[1]
    st.success(f"✅ Video ID Extracted: {video_id}")

col1, col2 = st.columns(2)

# Fetch Comments
with col1:
    if st.button("📥 Fetch Comments"):

        if video_id == "":
            st.error("Please enter a valid YouTube link!")

        else:

            comments = fetch_comments(video_id)

            st.success("Comments fetched successfully!")

            st.subheader("💬 Comments & Replies")

            for comment, reply in comments:

                with st.container():

                    st.markdown(f"**Comment:** {comment}")
                    st.markdown(f"**Reply:** {reply}")

                    st.divider()

# Show History
with col2:
    if st.button("📜 Show History"):

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

                st.subheader("📂 Comment History")

                for row in rows:

                    with st.container():

                        st.markdown(f"**ID:** {row[0]}")
                        st.markdown(f"**Comment:** {row[1]}")
                        st.markdown(f"**Reply:** {row[2]}")
                        st.markdown(f"**Video ID:** {row[3]}")

                        st.divider()

            else:
                st.warning("No records found!")

            conn.close()

st.markdown("---")
st.caption("YouTube Auto Reply Project | Python + SQLite + Streamlit")