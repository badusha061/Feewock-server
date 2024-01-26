from django.urls import path
from .views import GetMessage

urlpatterns = [  
    path('message/<int:sender_id>/<int:reciever_id>/', GetMessage.as_view(), name='text-message')

]
