
// Buttons Events
$(".leave-btn").click(() => window.location = "/conference/" + roomSlug);





function getWebSocketAddress() {
  const { protocol, hostname } = window.location;
  const port = window.location.port || (protocol === "https:" ? "443" : "80");
  const wsProtocol = protocol === "https:" ? "wss:" : "ws:";

  return `${wsProtocol}//${hostname}:${port}`;
}