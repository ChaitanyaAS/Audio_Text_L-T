const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const status = document.getElementById("status");
const transcriptDiv = document.getElementById("transcript");
const summaryDiv = document.getElementById("summary");

let mediaRecorder = null;
let audioChunks = [];
let stream = null;

// ==========================
// START RECORDING
// ==========================
startBtn.addEventListener("click", async () => {

    try {

        // Prevent double recording
        if (
            mediaRecorder &&
            mediaRecorder.state === "recording"
        ) {
            status.innerText = "Already Recording...";
            return;
        }

        transcriptDiv.innerText = "";
        summaryDiv.innerText = "";

        status.innerText =
            "Requesting Microphone...";

        stream =
            await navigator.mediaDevices.getUserMedia({
                audio: true
            });

        audioChunks = [];

        mediaRecorder =
            new MediaRecorder(stream);

        mediaRecorder.ondataavailable =
            (event) => {

                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

        mediaRecorder.onstart = () => {
            status.innerText =
                "Recording...";
            console.log("Recording Started");
        };

        mediaRecorder.start();

    }
    catch (error) {

        console.error(error);

        if (
            error.name === "NotAllowedError"
        ) {
            status.innerText =
                "Microphone Permission Denied";
        }
        else {
            status.innerText =
                "Unable to Access Microphone";
        }
    }
});


// ==========================
// STOP RECORDING
// ==========================
stopBtn.addEventListener("click", () => {

    if (
        !mediaRecorder ||
        mediaRecorder.state !== "recording"
    ) {
        status.innerText =
            "No Active Recording";
        return;
    }

    status.innerText =
        "Stopping Recording...";

    mediaRecorder.stop();
});


// ==========================
// AFTER RECORDING STOPS
// ==========================
if (mediaRecorder) {
    mediaRecorder.onstop = processAudio;
}

// Since mediaRecorder is created later,
// assign onstop inside start.
function attachStopHandler() {

    mediaRecorder.onstop =
        async function () {

            try {

                status.innerText =
                    "Preparing Audio...";

                console.log(
                    "Recording Stopped"
                );

                const audioBlob =
                    new Blob(
                        audioChunks,
                        {
                            type: "audio/webm"
                        }
                    );

                const formData =
                    new FormData();

                formData.append(
                    "audio",
                    audioBlob,
                    "meeting.webm"
                );

                status.innerText =
                    "Sending Audio...";

                const response =
                    await fetch(
                        "http://127.0.0.1:5000/process",
                        {
                            method: "POST",
                            body: formData
                        }
                    );

                if (!response.ok) {
                    throw new Error(
                        "Backend Error"
                    );
                }

                const data =
                    await response.json();

                console.log(data);

                transcriptDiv.innerText =
                    data.transcript ||
                    "No Transcript Generated";

                summaryDiv.innerText =
                    data.summary ||
                    "No MOM Generated";

                status.innerText =
                    "Completed";
            }
            catch (error) {

                console.error(error);

                status.innerText =
                    "Processing Failed";
            }
            finally {

                if (stream) {
                    stream
                        .getTracks()
                        .forEach(track =>
                            track.stop()
                        );
                }

                mediaRecorder = null;
                stream = null;
                audioChunks = [];
            }
        };
}


// ==========================
// PATCH START FUNCTION
// ==========================
const originalStart =
    startBtn.onclick;

startBtn.addEventListener(
    "click",
    () => {

        setTimeout(() => {

            if (
                mediaRecorder
            ) {
                attachStopHandler();
            }

        }, 200);
    }
);