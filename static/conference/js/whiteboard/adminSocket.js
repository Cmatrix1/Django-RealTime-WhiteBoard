

function connectWebSocket() {
  chatSocket = new WebSocket(
    getWebSocketAddress() +
    '/ws/board/' + roomSlug + '/'
  );
  chatSocket.onopen = function () {
    console.log('Board Socket connected!');
  };

  chatSocket.onclose = function () {
    console.log('Board Socket closed, retrying in 5 seconds...');
    setTimeout(connectWebSocket, 5000);
  };
}

function sendCanvas(canvas) {
  const imageData = canvas.toDataURL();
  const message = { imageData: imageData };
  chatSocket.send(JSON.stringify(message));
}

function addListener() {
  const canvas = document.querySelector("canvas");
  if (canvas) { 
      canvas.addEventListener("click", (e) => sendCanvas(e.target)) 
  }
}
connectWebSocket()
setTimeout(addListener, 2000);