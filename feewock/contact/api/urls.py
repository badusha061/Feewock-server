from django.urls import path
from .views import *

urlpatterns = [  
    path('contactuser', ContactFormUser.as_view(), name='contact'),

    path('contactadmin', ContactFormAdmin.as_view(), name='admin-contact')
]