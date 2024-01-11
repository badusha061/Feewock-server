from django.urls import path
from .views import CreateMainService ,UpdateMainservice , CreateSubService , UpdateSubservice , Postions , UpdatePositions

urlpatterns = [    
    path('createmainservice',CreateMainService.as_view() , name='createmain_serlizer'),
    path('updatemainservice/<int:pk>/',UpdateMainservice.as_view() , name='updatemain_serlizer'),

    path('subservice',CreateSubService.as_view() , name='createsub_serlizer'),
    path('updatesubervice/<int:pk>/',UpdateSubservice.as_view() , name='updatesub_serlizer'),
    path('postion',Postions.as_view() , name='positions'),
    path('updatepostion/<int:pk>/',UpdatePositions.as_view() , name='update_positions'),


]
