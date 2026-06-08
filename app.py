import streamlit as st
import sqlite3
from youtube_service import fetch_comments

st.title("YouTube Auto Reply Project")

# YouTube Link Input
link = st.text_input("Paste YouTube Link")

video_id = ""

if "v=" in link:
    video_id = link.split("v=")[1]

    st.success(f"Video ID Extracted: {video_id}")

# Fetch Comments Button
if st.button("Fetch Comments"):

    if video_id == "":
        st.error("Please enter a valid YouTube link!")

    else:

        comments = fetch_comments(video_id)

        st.success("Comments fetched and saved successfully!")

        for comment, reply in comments:

            st.write("Comment:", comment)
            st.write("Reply:", reply)
            st.write("------------------------")

# Show History Button
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