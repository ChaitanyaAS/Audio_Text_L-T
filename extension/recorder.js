let recorder;
let chunks = [];

async function startRecording() {

    const stream =
        await navigator.mediaDevices.getUserMedia({
            audio: true
        });

    recorder = new MediaRecorder(stream);

    recorder.ondataavailable = e => {
        chunks.push(e.data);
    };

    recorder.start();
}

function stopRecording() {

    return new Promise(resolve => {

        recorder.onstop = () => {

            const blob =
                new Blob(
                    chunks,
                    {
                        type: "audio/wav"
                    }
                );

            chunks = [];

            resolve(blob);
        };

        recorder.stop();
    });
}