from django.urls import path , include
from .views import UserViewSet
from .views import *
from rest_framework_simplejwt.views import (
   TokenRefreshView,
)


urlpatterns = [    
    path('userindivual/<int:pk>/',UserIndivualView.as_view(), name='token_refersh'),
    path('notification/<int:pk>/', UserNotificationCount.as_view(), name='user-notification'),
    path('userimages/<int:pk>/',UserIndivualImage.as_view(), name='token_refersh'),
    path('token',CustomerTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refersh/',TokenRefreshView.as_view(), name='token_refersh'),
]
