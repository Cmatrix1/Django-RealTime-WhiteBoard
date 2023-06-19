from django.urls import path, re_path

from whiteboard import consumers

websocket_urlpatterns = [
    path('ws/board/', consumers.BoardConsumer.as_asgi()),
    re_path(r'ws/message/(?P<slug>[\w-]+)/$', consumers.MessageConsumer.as_asgi()),
]