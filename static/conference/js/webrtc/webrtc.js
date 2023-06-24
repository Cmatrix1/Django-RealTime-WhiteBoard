// const stopCameraButton = document.querySelector("")
const stopMicButton = document.querySelector("usr-img-bottom-btn")

navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(function (stream) {
        var videoBox = document.getElementById('my-videoBox');
        videoBox.srcObject = stream;
    })
    .catch(function (err) {
        console.log(err);
    }
    );

stopCameraButton.addEventListener('click', function () {
    const videoTrack = mediaStream.getVideoTracks()[0];
    videoTrack.stop();
});

stopMicButton.addEventListener('click', function (e) {
    const audioTrack = mediaStream.getAudioTracks()[0];
    audioTrack.stop();
    e.target.style.color = "red";
});