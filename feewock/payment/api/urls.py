from django.urls import path
from .views import *

urlpatterns = [  
    path('create-checkout-session/<int:pk>/', StripeCheckoutView.as_view()),
]

