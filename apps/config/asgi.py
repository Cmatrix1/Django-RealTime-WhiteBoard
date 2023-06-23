import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack # Import the SessionMiddlewareStack
from board.routing import websocket_urlpatterns as board_websocket_urlpatterns
from message.routing import websocket_urlpatterns as message_websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            SessionMiddlewareStack( 
                URLRouter(
                    board_websocket_urlpatterns + message_websocket_urlpatterns
                )
            )
        ),
    }
)
