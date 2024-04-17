import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feewock.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter 
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import TextConsumer , NoficationEmployee , NoficationUser
from django.urls import re_path
from channels.auth import AuthMiddleware , SessionMiddleware , AuthMiddlewareStack
from django.core.asgi import get_asgi_application



websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[\w_]+)/$', TextConsumer.as_asgi()),
    re_path(r'^ws/notification/(?P<employee_id>\w+)/$', NoficationEmployee.as_asgi()),
    re_path(r'^ws/notificationuser/(?P<userId>\w+)/$', NoficationUser.as_asgi()),
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