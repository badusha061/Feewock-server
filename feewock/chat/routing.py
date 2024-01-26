from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import TextConsumer
from django.urls import re_path
import os
from channels.auth import AuthMiddleware , SessionMiddleware , AuthMiddlewareStack
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feewock.settings')

websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', TextConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )        
}
)