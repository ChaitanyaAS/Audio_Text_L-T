
# Audio_Text_L-T

An intelligent Audio-to-Text transcription and translation system featuring a browser extension frontend and a powerful Python backend. The project utilizes OpenAI's Whisper model to deliver seamless speech-to-text capabilities in both **online** and **offline** environments.

---

## Features

* **Dual Processing Modes:** * `Online Mode`: Leverages cloud/API endpoints for quick, resource-efficient transcriptions.
    * `Offline Mode`: Runs locally using pre-downloaded Whisper models for complete privacy and data control.
* **Browser Extension:** A lightweight frontend (`JavaScript`, `HTML`, `CSS`) allowing users to capture and send audio directly from their browser.
* **Local Model Management:** Dedicated utility script to pull and set up Whisper models locally.

---

##  Repository Structure

```text
├── backend/               # Python server managing transcription & translation logic
├── extension/             # Browser extension frontend (manifest, popup, background scripts)
├── models/whisper/        # Directory where local Whisper model weights are stored
├── output/                # Directory where generated text/transcription files are saved
├── download_whisper.py    # Utility script to download Whisper models for offline use
├── offline_mode.py        # Logic for processing audio locally without internet
├── online_mode.py         # Logic for processing audio using online APIs
└── requirements.txt       # Python dependencies

```

---

## Prerequisites

Before getting started, ensure you have the following installed:

* [Python 3.8+](https://www.python.org/)
* [FFmpeg](https://ffmpeg.org/) (Required by Whisper for audio processing)
* A modern web browser (Chrome/Edge/Brave) for loading the extension.

---

##  Installation & Setup

### 1. Backend Setup

1. Clone the repository:
```bash
git clone [https://github.com/ChaitanyaAS/Audio_Text_L-T.git](https://github.com/ChaitanyaAS/Audio_Text_L-T.git)
cd Audio_Text_L-T

```


2. Install the required Python dependencies:
```bash
pip install -r requirements.txt

```


3. **(Optional) Setup Offline Mode:** If you plan to run the transcription locally without an internet connection, download the Whisper model weights:
```bash
python download_whisper.py

```



### 2. Browser Extension Setup

1. Open your browser and navigate to the Extensions page (e.g., `chrome://extensions/` for Chrome).
2. Enable **Developer mode** (usually a toggle switch in the top-right corner).
3. Click on **Load unpacked** and select the `extension` folder from this repository.

---

##  Usage

1. **Start the Backend Server:**
Run the backend server to begin listening for incoming audio requests from the extension:
```bash
python online_mode.py   # For online API processing
# OR
python offline_mode.py  # For local/offline processing

```


2. **Interact via Browser:**
Click the extension icon in your browser toolbar to capture audio, submit it, and view the transcribed text output.
3. **Outputs:**
Transcribed files will be saved systematically in the `output/` directory.

---

##  Built With

* **Backend:** Python, OpenAI Whisper
* **Frontend:** JavaScript, HTML5, CSS3

---

##  License

This project is open-source. Please check the repository settings or add a `LICENSE` file for specific terms.

```

***

###  Tips for Customization:
* **Backend Framework:** If your backend uses a specific framework like Flask or FastAPI inside the `backend/` folder, mention it under **Built With**.
* **Ports:** If your server runs on a specific port (e.g., `http://localhost:5000`), you can add that to the **Usage** section so users know exactly where the extension is pointing.

```
