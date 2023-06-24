let image = document.querySelector('.board-img')

function connectWebSocket() {
    chatSocket = new WebSocket(
      getWebSocketAddress() +
      '/ws/board/' + roomSlug + '/'
    );
    chatSocket.onopen = function () {
      console.log('Board Socket connected!');
    };

    chatSocket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        image.src = data.imageData;
        console.log("Board Socket Recive !");
    };

    chatSocket.onclose = function () {
      console.log('Board Socket closed, retrying in 5 seconds...');
      setTimeout(connectWebSocket, 5000);
    };
  }
  
connectWebSocket()