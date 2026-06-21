import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import datetime
from transcription import transcribe_audio
from backend.summarizer import generate_summary
def run_online_mode():
    print("\n===== ONLINE MEETING MODE =====")
    input("\nPress ENTER to start recording...")
    fs = 16000
    print("\nRecording Started...")
    print("Press ENTER again to stop recording.\n")
    recording = []
    def callback(indata, frames, time, status):
        recording.append(indata.copy())
    stream = sd.InputStream(
        samplerate=fs,
        channels=1,
        callback=callback
    )
    stream.start()
    input()
    stream.stop()
    stream.close()
    print("\nRecording Stopped")
    audio = np.concatenate(recording, axis=0)
    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )
    audio_file = f"input/meetings/live_{timestamp}.wav"
    write(
        audio_file,
        fs,
        audio
    )
    print(f"\nSaved: {audio_file}")
    print("\nTranscribing...")
    transcript = transcribe_audio(audio_file)
    print("\nGenerating MOM...")
    summary = generate_summary(transcript)
    print("\n========== FINAL REPORT ==========\n")
    print(summary)