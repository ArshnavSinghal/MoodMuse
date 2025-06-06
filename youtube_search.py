# app/youtube_search.py
from googleapiclient.discovery import build
import webbrowser

YOUTUBE_API_KEY = "AIzaSyDo0FBSGZUwRx1l0rQuKzMVBpRuIoj-uIc"

def search_youtube_music(query):
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=1,
            videoCategoryId="10"
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(url)
    except Exception as e:
        print(f"Error using YouTube API: {e}")
