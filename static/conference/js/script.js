
// Buttons Events
$(".leave-btn").click(() => window.location = "/conference/" + roomSlug);





function getWebSocketAddress() {
  const { protocol, hostname } = window.location;
  const port = window.location.port || (protocol === "https:" ? "443" : "80");
  const wsProtocol = protocol === "https:" ? "wss:" : "ws:";

  return `${wsProtocol}//${hostname}:${port}`;
}



const notification = document.querySelector('#notification')
const text = document.querySelector('#notification-text')
const icon = document.querySelector('#notification-icon')

const showNotification = (t) => {
	text.textContent = t
	notification.classList.add('show')
	setTimeout(() => {
		notification.classList.remove('show')
	}, 2500)
}