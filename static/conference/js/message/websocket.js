const chatBox = document.getElementById('chat-box');
const messageInp = document.getElementById('message-input');
const username = document.getElementById('username');

let chatSocket;

function handleOnMessage(e) {
  const data = JSON.parse(e.data);
  const { username, message } = data;
  const options = { hour: 'numeric', minute: 'numeric' };
  const messageHTML = `
  <div class="message">
    <div class="message-header">
      <div class="author">${username}</div>
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