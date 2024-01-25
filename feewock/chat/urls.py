from django.urls import path
from .views import TextMessage

urlpatterns = [  
    path('message', TextMessage.as_view() , name='text-message')
]
