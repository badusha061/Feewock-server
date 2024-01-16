from django.urls import path 
from .views import *

urlpatterns = [
    #User    
    path('userlist',UserListView.as_view() , name='userlist'),
    path('userlist/<int:pk>/block',UserBlockUnblock.as_view({'put':'block'}) , name='userblock'),
    path('userlist/<int:pk>/unblock',UserBlockUnblock.as_view({'put':'unblock'}) , name='userunblock'),


    #Employee
    path('employeelist',EmployeesListView.as_view(), name='employee-list'),
    path('employeelist/<int:pk>/block',EmployeeBlockUnblock.as_view({'put':'block'}) , name='userblock'),
    path('employeelist/<int:pk>/unblock',EmployeeBlockUnblock.as_view({'put':'unblock'}) , name='userunblock'),
]
