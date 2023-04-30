
const socket = new WebSocket('ws://localhost:8000/ws/board/');
let image = document.getElementById('userImage');

socket.addEventListener('open', (event) => {
    console.log('WebSocket connection established');
});

socket.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    image.src = data.imageData;
    console.log("recive");
});

socket.addEventListener('close', (event) => {
    console.log('WebSocket connection closed');
});