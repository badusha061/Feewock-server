from django.urls import path
from .views import *

urlpatterns = [  
    path('adminlist', AdminDashboard.as_view(), name='admin-dashboard'),
]
