import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from . import consumers, routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "channel": ChannelNameRouter(
            {
                "experiment": consumers.PrintConsumer.as_asgi(),
            }
        ),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
