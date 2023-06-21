function getWebsiteURLWithPort() {
    // const { protocol, hostname, port } = window.location;
    // return `${protocol}//${hostname}${port ? `:${port}` : ""}`;
    return 'http://127.0.0.1:8000'
}

async function fetchMessages(roomName) {
    const response = await fetch(`${getWebsiteURLWithPort()}/api/${roomName}/messages/`);
    const messages = await response.json();

    const chatBox = document.getElementById('chat-box');
    const options = { hour: 'numeric', minute: 'numeric' };
    const messageHtmls = messages.map(({ sender, created_at, content }) => `
      <div class="message">
        <div class="message-header">
          <div class="author">${sender}</div>
          <div class="date">${new Date(created_at).toLocaleTimeString('en-US', options)}</div>
        </div>
        <div class="message-body small">
          <p>${content}</p>
        </div>
      </div>
    `);
    chatBox.innerHTML += messageHtmls.join('');
}

fetchMessages("test")


