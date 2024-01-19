from django.urls import path 
from .views import ListEmployees


urlpatterns = [    
  path('employees/<int:service_id>/',ListEmployees.as_view(),name='list-employee-userside')
]
