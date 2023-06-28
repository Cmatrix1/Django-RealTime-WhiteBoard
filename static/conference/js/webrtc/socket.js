// Initialize variables
let localStream;
let remoteStreams = [];

const socket = new WebSocket('ws://' + "127.0.0.1:8000" + '/ws/message/' + roomSlug + '/');

// Configure WebRTC connection
const configuration = {
  iceServers: [
    { urls: 'stun:stun.stunserver.org:3478' },
    { urls: 'stun:stun.l.google.com:19302' },
  ],
};

// Create a new RTCPeerConnection instance
const peerConnection = new RTCPeerConnection(configuration);

// Add local stream to the peer connection
function addLocalStream(stream) {
  localStream = stream;
  localStream.getTracks().forEach(track => {
    peerConnection.addTrack(track, localStream);
  });
}

// Handle incoming remote stream
function handleRemoteStream(event) {
  const stream = event.streams[0];
  remoteStreams.push(stream);
  // Display remote stream in a video element
  const videoElement = document.createElement('video');
  videoElement.srcObject = stream;
  videoElement.autoplay = true;
  videoElement.controls = true;
  document.getElementById('remoteVideos').appendChild(videoElement);
}

// Start the WebRTC negotiation process
async function startWebRTC() {
  try {
    // Get local media stream
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    addLocalStream(stream);

    // Send the offer SDP (Session Description Protocol)
    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);

    // Send the offer to the server or another peer
    socket.emit('offer', offer);
  } catch (error) {
    console.error('Error accessing media devices:', error);
  }
}

// Receive the answer SDP from the server or another peer
socket.on('answer', async answer => {
  await peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
});

// Handle ICE (Interactive Connectivity Establishment) candidates
socket.on('candidate', candidate => {
  peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
});

// Listen for remote stream event
peerConnection.addEventListener('track', handleRemoteStream);

// Send ICE candidates to the server or another peer
peerConnection.addEventListener('icecandidate', event => {
  if (event.candidate) {
    socket.emit('candidate', event.candidate);
  }
});
