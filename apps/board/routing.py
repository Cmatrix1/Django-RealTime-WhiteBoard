from django.urls import path, re_path

from board import consumers

websocket_urlpatterns = [
    path('ws/board/', consumers.BoardConsumer.as_asgi()),
]