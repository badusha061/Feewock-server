from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import TextConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', TextConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})