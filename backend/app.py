from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

from transcription import transcribe_audio
from summarizer import generate_summary

app = Flask(__name__)
CORS(app)

# ==========================================
# CREATE REQUIRED FOLDERS
# ==========================================

os.makedirs("../input/meetings", exist_ok=True)
os.makedirs("../output/transcripts", exist_ok=True)
os.makedirs("../output/summaries", exist_ok=True)
os.makedirs("../output/reports", exist_ok=True)

# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "service": "Meeting Intelligence Backend",
        "message": "Backend is working successfully"
    })


# ==========================================
# TRANSCRIBE AUDIO ONLY
# ==========================================

@app.route("/transcribe", methods=["POST"])
def transcribe():

    if "audio" not in request.files:
        return jsonify({
            "success": False,
            "message": "No audio file received"
        }), 400

    audio = request.files["audio"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"meeting_{timestamp}.wav"

    filepath = os.path.join(
        "../input/meetings",
        filename
    )

    audio.save(filepath)

    print("\nAudio Saved:")
    print(filepath)

    transcript = transcribe_audio(filepath)

    return jsonify({
        "success": True,
        "audio_file": filename,
        "transcript": transcript
    })


# ==========================================
# GENERATE MOM ONLY
# ==========================================

@app.route("/summary", methods=["POST"])
def summary():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No JSON data received"
        }), 400

    transcript = data.get("transcript")

    if not transcript:
        return jsonify({
            "success": False,
            "message": "Transcript missing"
        }), 400

    summary_text = generate_summary(transcript)

    return jsonify({
        "success": True,
        "summary": summary_text
    })


# ==========================================
# COMPLETE PIPELINE
# ==========================================

@app.route("/process", methods=["POST"])
def process():

    if "audio" not in request.files:
        return jsonify({
            "success": False,
            "message": "No audio file received"
        }), 400

    audio = request.files["audio"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"meeting_{timestamp}.wav"

    filepath = os.path.join(
        "../input/meetings",
        filename
    )

    audio.save(filepath)

    print("\nAudio Saved:")
    print(filepath)

    print("\nStep 1 : Transcribing")
    transcript = transcribe_audio(filepath)

    print("\nStep 2 : Generating MOM")
    summary_text = generate_summary(transcript)

    return jsonify({
        "success": True,
        "audio_file": filename,
        "transcript": transcript,
        "summary": summary_text
    })


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )