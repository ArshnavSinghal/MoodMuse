# app/music_generator.py
from app.youtube_search import search_youtube_music

EMOTION_TO_MUSIC = {
    "Happy": "upbeat happy pop music",
    "Sad": "sad acoustic guitar",
    "Angry": "intense rock music",
    "Fear": "dark ambient background music",
    "Surprise": "exciting electronic dance music",
    "Neutral": "chill lo-fi beats",
    "Disgust": "moody alternative",
}

def generate_music_from_emotion(emotion):
    query = EMOTION_TO_MUSIC.get(emotion, "calm music")
    print(f"🎵 Searching YouTube for: {query}")
    search_youtube_music(query)
