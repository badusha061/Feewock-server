from django.urls import path
from .views import *

urlpatterns = [    
    path('employeeupdate/<int:pk>/',EmployeeUpdateImage.as_view(),name='employee-update'),
    path('employeeedit/<int:pk>/',EmployeeUpdate.as_view(),name='employee-update'),
    path('employeeavailability', EmployeesAvailabilityView.as_view() , name='empoloyee-availibiilty'),     
    path('indivual/<int:pk>/', EmployeesAvailabilityViewIndivual.as_view() , name='empoloyee-availibiilty'),     
    path('delete/<int:pk>/', EmployeesAvailabilityViewIndivualDelete.as_view() , name='empoloyee-availibiilty'),   
    path('notification/<int:pk>/', NotificationCount.as_view(), name='employee-notification'),
]
