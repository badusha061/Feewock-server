from django.urls import path
from .views import ListUserBanner , UpdateUserBanner

urlpatterns = [  
    path('list', ListUserBanner.as_view(), name='list-banner'),
    path('update/<int:pk>/', UpdateUserBanner.as_view(), name='update-banner')

]