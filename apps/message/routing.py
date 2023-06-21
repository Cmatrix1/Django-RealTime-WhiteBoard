from django.urls import path, re_path

from message import consumers

websocket_urlpatterns = [
    re_path(r'ws/message/(?P<slug>[\w-]+)/$', consumers.MessageConsumer.as_asgi()),
]