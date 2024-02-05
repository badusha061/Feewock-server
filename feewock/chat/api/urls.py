from django.urls import path
from .views import GetMessage , GetEmployeeMessage , Is_read

urlpatterns = [  
    path('message/<int:sender_id>/<int:reciever_id>/', GetMessage.as_view(), name='text-message'),
    path('employeemessage/<int:pk>/', GetEmployeeMessage.as_view(), name='employee-messsage'),
    path('is_read/<int:pk>/', Is_read.as_view(), name='is_read')
]
