from django.urls import path
from .views import *

urlpatterns = [   
    # Main service 
    path('createmainservice', CreateMainService.as_view(), name='createmain_serlizer'),
    path('updatemainservice/<int:pk>/', UpdateMainservice.as_view(), name='updatemain_serlizer'),

    # Sub Service
    path('subservice', ListSubService.as_view(), name='listingsub_serlizer'),
    path('subserviceemployee', ListSubServiceEmployee.as_view(), name='listingsub_serlizer'),
    path('createsubservice', CreateSubService.as_view(), name='creatingsub-service'), 
    path('updatesubervice/<int:pk>/', UpdateSubservice.as_view(), name='updatesub_serlizer'),

    #user listing sub service 
    path('updatesuberviceuser/<int:pk>/', UpdateSubserviceUser.as_view(), name='updatesub_serlizer'),


    # Positions
    path('postion', Postions.as_view(), name='positions'),
    path('updatepostion/<int:pk>/', UpdatePositions.as_view(), name='update_positions'),

    path('list',ListingMainService.as_view() , name='listing'),
    path('userlist',ListingUserMainService.as_view() , name='listing')
]
