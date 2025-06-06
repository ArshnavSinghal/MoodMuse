# app/app.py

from flask import Flask, render_template, Response, request, jsonify
import cv2
from app.emotion_detector import detect_emotion_from_frame
from app.music_generator import generate_music_from_emotion

camera = cv2.VideoCapture(0)

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    def gen_frames():
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                _, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    @app.route('/video_feed')
    def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/detect_emotion', methods=['POST'])
    def detect_emotion():
        success, frame = camera.read()
        if success:
            emotion = detect_emotion_from_frame(frame)
            return jsonify({'emotion': emotion})
        return jsonify({'emotion': 'Unknown'})

    @app.route('/generate_music', methods=['POST'])
    def generate_music():
        data = request.get_json()
        emotion = data.get('emotion', 'Neutral')
        generate_music_from_emotion(emotion)
        return jsonify({'status': 'Music generated for ' + emotion})

    return app
