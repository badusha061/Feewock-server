from django.urls import path 
from .views import *

urlpatterns = [    
    path('create', Reviews.as_view(), name='reviews'),
    path('list/<int:pk>/', ReviewsUserSide.as_view(), name='listing-user-side')
]
