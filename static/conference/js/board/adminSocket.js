const App = () => {
    return React.createElement(
        React.Fragment,
        null,
        React.createElement(
            "div",
            {
                style: { height: "100%" },
            },
            React.createElement(ExcalidrawLib.Excalidraw)
        )
    );
};

const excalidrawWrapper = document.getElementById("app");
const root = ReactDOM.createRoot(excalidrawWrapper);
root.render(React.createElement(App));

function connectWebSocket() {
  boardSocket = new WebSocket(
    getWebSocketAddress() +
    '/ws/board/' + roomSlug + '/'
  );
  boardSocket.onopen = function () {
    console.log('Board Socket connected!');
  };

  boardSocket.onclose = function () {
    console.log('Board Socket closed, retrying in 5 seconds...');
    setTimeout(connectWebSocket, 5000);
  };
}

function sendCanvas(canvas) {
  const imageData = canvas.toDataURL();
  const message = { imageData: imageData };
  boardSocket.send(JSON.stringify(message));
}


function addListener() {
  const canvas = document.querySelector("canvas");
  if (canvas) { 
      canvas.addEventListener("click", (e) => sendCanvas(e.target)) 
  }
}
connectWebSocket()
setTimeout(addListener, 2000);