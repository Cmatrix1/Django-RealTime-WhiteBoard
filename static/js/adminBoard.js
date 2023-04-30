const App = () => {
    return React.createElement(
        React.Fragment,
        null,
        React.createElement(
            "div",
            {
                style: { height: "500px" },
            },
            React.createElement(ExcalidrawLib.Excalidraw)
        )
    );
};

const excalidrawWrapper = document.getElementById("app");
const root = ReactDOM.createRoot(excalidrawWrapper);
root.render(React.createElement(App));




const socket = new WebSocket('ws://localhost:8000/ws/board/');
function sendCanvas(canvas) {
    const imageData = canvas.toDataURL();
    const message = { imageData: imageData };
    socket.send(JSON.stringify(message));
}

function addListener() {
    const canvas = document.querySelector("canvas");
    if (canvas) { 
        canvas.addEventListener("click", (e) => sendCanvas(e.target)) 
    }
}

setTimeout(addListener, 2000);