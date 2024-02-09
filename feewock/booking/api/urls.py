from django.urls import path
from .views import appointment ,EmployeeAppointment , EmployeeActionList , EmployeeActionIndivual , UserAppointment

urlpatterns = [  

    path('appointment', appointment.as_view(), name='appoitment'),
    path('appointment/<int:pk>/', EmployeeAppointment.as_view() , name='employee-appointment'),
    path('userlist/<int:pk>/', UserAppointment.as_view(), name='user-actions'),
    path('action', EmployeeActionList.as_view() , name='employee-actions'),
    path('user/<int:pk>/', EmployeeActionIndivual.as_view() , name='employee-actions'),
]
