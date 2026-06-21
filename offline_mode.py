import os
from transcription import transcribe_audio
from backend.summarizer import generate_summary
def run_offline_mode():
    folder = "input/meetings"
    files = [
        f for f in os.listdir(folder)
        if f.endswith((".mp3", ".wav"))
    ]
    if not files:
        print("No recordings found.")
        return
    print("\nAvailable Recordings:\n")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    choice = int(input("\nSelect Recording: "))
    selected_file = files[choice - 1]
    audio_path = os.path.join(folder, selected_file)
    print("\nTranscribing...\n")
    transcript = transcribe_audio(audio_path)
    print("\nGenerating MOM...\n")
    summary = generate_summary(transcript)
    print(summary)