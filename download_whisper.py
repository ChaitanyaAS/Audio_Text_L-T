from faster_whisper import WhisperModel
model = WhisperModel(   
    "small",
    device="cpu",
    compute_type="int8",
    download_root="models/whisper"
)
print("Whisper Download Complete")