let image = document.querySelector('.board-img')

function connectWebSocket() {
    boardSocket = new WebSocket(
      getWebSocketAddress() +
      '/ws/board/' + roomSlug + '/'
    );
    boardSocket.onopen = function () {
      console.log('Board Socket connected!');
    };

    boardSocket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        image.src = data.imageData;
        console.log("Board Socket Recive !");
    };

    boardSocket.onclose = function () {
      console.log('Board Socket closed, retrying in 5 seconds...');
      setTimeout(connectWebSocket, 5000);
    };
  }
  
connectWebSocket()