from django.urls import path

from whiteboard import consumers

websocket_urlpatterns = [
    path('ws/board/', consumers.BoardConsumer.as_asgi()),
]