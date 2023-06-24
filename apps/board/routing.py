from django.urls import path, re_path

from board import consumers

websocket_urlpatterns = [
    re_path(r'ws/board/(?P<slug>[\w-]+)/$', consumers.BoardConsumer.as_asgi()),
]