from django.urls import path
from .views import PaymentAPI

urlpatterns = [  
    path('strip', PaymentAPI.as_view(), name='payment'),    
]
