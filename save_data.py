import sqlite3

DB_NAME = "youtube.db"


def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Keywords Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS keywords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT,
        search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Videos Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos(
        video_id TEXT PRIMARY KEY,
        title TEXT,
        channel_name TEXT,
        published_at TEXT,
        keyword TEXT
    )
    """)

    # Comments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments(
        comment_id TEXT PRIMARY KEY,
        video_id TEXT,
        author TEXT,
        comment TEXT,
        timestamp TEXT,
        processed INTEGER DEFAULT 0
    )
    """)

    # Replies Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS replies(
        reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment_id TEXT,
        reply_text TEXT,
        status TEXT,
        posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_keyword(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO keywords(keyword) VALUES(?)",
        (keyword,)
    )

    conn.commit()
    conn.close()


def save_video(video_id, title, channel_name, published_at, keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO videos
    (video_id, title, channel_name, published_at, keyword)
    VALUES (?, ?, ?, ?, ?)
    """, (video_id, title, channel_name, published_at, keyword))

    conn.commit()
    conn.close()


def save_comment(comment_id, video_id, author, comment, timestamp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO comments
    (comment_id, video_id, author, comment, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (comment_id, video_id, author, comment, timestamp))

    conn.commit()
    conn.close()


def save_reply(comment_id, reply_text, status="Pending"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO replies
    (comment_id, reply_text, status)
    VALUES (?, ?, ?)
    """, (comment_id, reply_text, status))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("✅ Database Created Successfully")