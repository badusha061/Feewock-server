from django.urls import path
from .views import Employees 

urlpatterns = [    
    path('create',Employees.as_view(), name='create_employee'),

]
