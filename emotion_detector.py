# app/emotion_detector.py
from deepface import DeepFace
import cv2

def detect_emotion_from_frame(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion'].capitalize()
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return "Neutral"
