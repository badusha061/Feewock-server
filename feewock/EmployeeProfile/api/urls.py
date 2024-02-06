from django.urls import path
from .views import EmployeeUpdateImage , EmployeeUpdate , EmployeesAvailabilityView

urlpatterns = [    
    path('employeeupdate/<int:pk>/',EmployeeUpdateImage.as_view(),name='employee-update'),
    path('employeeedit/<int:pk>/',EmployeeUpdate.as_view(),name='employee-update'),
    path('employeeavailability', EmployeesAvailabilityView.as_view() , name='empoloyee-availibiilty')      
]
