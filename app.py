import streamlit as st
import sqlite3

st.title("YouTube Auto Reply Project")

video_id = st.text_input("Enter Video ID")

if st.button("Show History"):

    conn = sqlite3.connect("youtube.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM comments WHERE video_id=?",
        (video_id,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            st.write("ID:", row[0])
            st.write("Comment:", row[1])
            st.write("Reply:", row[2])
            st.write("Video ID:", row[3])
            st.write("------------------------")
    else:
        st.warning("No records found!")

    conn.close()