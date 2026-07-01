# 🎥 YouTube Auto Reply System

A Python-based application that fetches YouTube comments, generates automatic replies, stores data in SQLite, provides analytics through a Streamlit dashboard, and exports comment history to CSV.

---

## 🚀 Features

- 🔍 Search YouTube videos using keywords
- 💬 Fetch comments from YouTube videos
- 🤖 Generate automatic replies based on keywords
- 🗄️ Store comments and replies in SQLite
- 🚫 Prevent duplicate comments using Comment ID
- 📊 Analytics Dashboard
  - Total Videos Scanned
  - Total Comments Collected
  - Total Replies Generated
  - Pending Replies
  - Posted Replies
  - Failed Replies
- 📥 Export comments and replies to CSV
- 😊 Sentiment Analysis using TextBlob
- 🎥 View video details such as title, views, likes, and publish date
- 🔮 Future Enhancement: Gemini AI-generated replies

---

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- YouTube Data API v3
- Pandas
- TextBlob
- Matplotlib
- Google Gemini API (Future Integration)

---

## 📂 Project Structure

```text
YouTube_AutoReply_Project/

├── app.py
├── auto_reply.py
├── comment_analysis.py
├── comments.py
├── config.py
├── export_csv.py
├── save_data.py
├── search_video.py
├── video_details.py
├── youtube_service.py
├── requirements.txt
├── README.md
└── youtube.db
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YouTube_AutoReply_Project.git
cd YouTube_AutoReply_Project
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Open `config.py` and add your YouTube API key:

```python
API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the local URL in your browser.

---

## 📊 Dashboard Features

The Streamlit dashboard provides:

- Total Videos Scanned
- Total Comments Collected
- Total Replies Generated
- Pending Replies
- Posted Replies
- Failed Replies
- Comment History
- CSV Export

---

## 📥 CSV Export

The application can export comment history as:

```text
comments_history.csv
```

The exported file contains:

- Comment ID
- Video ID
- Author
- Comment
- Timestamp
- Generated Reply
- Reply Status

---

## 🔮 Future Improvements

- Gemini AI-generated replies
- Automatic posting of replies on YouTube
- Advanced analytics and charts
- Multi-language support
- User authentication

---

## 👨‍💻 Team Members

- Tanmay Aggarwal
- Jyoti Saini

---

## 📜 License

This project was developed for educational and internship purposes.