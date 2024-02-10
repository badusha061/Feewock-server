from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import TextConsumer , NoficationEmployee , NoficationUser
from django.urls import re_path
import os
from channels.auth import AuthMiddleware , SessionMiddleware , AuthMiddlewareStack
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feewock.settings')

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[\w_]+)/$', TextConsumer.as_asgi()),
    re_path(r'^ws/notification/(?P<employee_id>\w+)/$', NoficationEmployee.as_asgi()),
    re_path(r'^ws/notificationuser/(?P<room_name>\w+)/$', NoficationUser.as_asgi()),
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