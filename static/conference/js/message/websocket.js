const chatBox = document.getElementById('chat-box');
const messageInp = document.getElementById('message-input');
const username = document.getElementById('username');
// for test
const roomSlug = "test";
let chatSocket;

function handleOnMessage(e) {
  const data = JSON.parse(e.data);
  console.log("OnMessage Run !", data);

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


function addUserMessage(message) {
  const options = { hour: 'numeric', minute: 'numeric' };
  const messageHTML = `
  <div class="user-message">
    <div class="message-header">
      <div class="author">${username.textContent}</div>
      <div class="date">${new Date().toLocaleTimeString('en-US', options)}</div>
    </div>
    <div class="message-body small">
      <p>${message}</p>
    </div>
  </div>
`;
  chatBox.innerHTML += messageHTML;
  chatBox.scroll({
    top: chatBox.scrollHeight,
    behavior: 'smooth'
  });
}

function sendMessage(e) {
  e.preventDefault();
  const content = messageInp.value
  messageInp.value = ""
  const message = {
    'message': content
  };
  addUserMessage(content)
  chatSocket.send(JSON.stringify(message));

}

document.getElementById("send-msg-btn").onclick = (e) => sendMessage(e)