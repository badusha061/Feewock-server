from django.urls import path 
from .views import Registrations

urlpatterns = [    
    path('register/',Registrations.as_view() , name='register'),
     
]
