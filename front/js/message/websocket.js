const chatBox = document.getElementById('chat-box');
const messageInp = document.getElementById('message-input');
const username = document.getElementById('username');
// for test
const roomSlug = "test";
let chatSocket;

function handleOnMessage(e) {
    const data = JSON.parse(e.data);
    const { sender, content, created_at } = data;

    // Add the message to the chat box
    const options = { hour: 'numeric', minute: 'numeric' };
    const messageHTML = `
  <div class="message">
    <div class="message-header">
      <div class="author">${sender}</div>
      <div class="date">${new Date(created_at).toLocaleTimeString('en-US', options)}</div>
    </div>
    <div class="message-body small">
      <p>${content}</p>
    </div>
  </div>
`;
    chatBox.innerHTML += messageHTML;
};

function connectWebSocket() {
    chatSocket = new WebSocket(
        'ws://' + "127.0.0.1:8000" +
        '/ws/message/' + roomSlug + '/'
    );
    chatSocket.onopen = function () {
        console.log('WebSocket connected!');
    };

    chatSocket.onmessage = e => handleOnMessage(e)

    chatSocket.onclose = function () {
        console.log('WebSocket closed, retrying in 5 seconds...');
        setTimeout(connectWebSocket, 5000);
    };
}

connectWebSocket();


function sendMessage(e) {
    console.log(e);
    console.log("I run");
    e.preventDefault();
    const content = messageInp.value
    const message = {
        'message': content
    };
    chatSocket.send(JSON.stringify(message));
}

// document.getElementById("send-msg-btn").onclick = (e) => sendMessage(e)