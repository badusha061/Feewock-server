from django.urls import path 
from .views import Registrations
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import *



urlpatterns = [    
    path('register/',Registrations.as_view() , name='register'),
    path('token',TokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refersh/',TokenRefreshView.as_view(), name='token_refersh'),
     
]
