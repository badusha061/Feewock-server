from django.urls import path
from .views import *

urlpatterns = [  

    path('appointment', appointment.as_view(), name='appoitment'),
    path('appointment/<int:pk>/', EmployeeAppointment.as_view() , name='employee-appointment'),
    path('userlist/<int:pk>/', UserAppointment.as_view(), name='user-actions'),
    path('action', EmployeeActionList.as_view() , name='employee-actions'),
    path('user/<int:pk>/', EmployeeActionIndivual.as_view() , name='employee-actions'),
    path('indivual/<int:pk>/' ,IndivualAction.as_view(), name='indivual-action'),

    path('stripsuccess/<int:pk>/' , Strip_Payment.as_view(), name='strip-payment'),
    path('cashondelivery/<int:pk>/' , CashOnDelivery.as_view(), name='cash-payment'),

    #admin side listing
    path('adminorderlist', AdminOrderList.as_view(), name='admin-listing' ),
    path('adminindivualorderlist/<int:pk>/', AdminOrderListIndivual.as_view(), name='admin-listing' ),



]
