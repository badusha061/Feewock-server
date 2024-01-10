from django.urls import path
from .views import CreateMainService ,UpdateMainservice , CreateSubService , MainServiceSerializer

urlpatterns = [    
    path('createmainservice',CreateMainService.as_view() , name='createmain_serlizer'),
    path('updatemainservice/<int:pk>/',UpdateMainservice.as_view() , name='updatemain_serlizer'),

    path('createsubservice',CreateSubService.as_view() , name='createsub_serlizer'),
    path('updatesubervice/<int:pk>/',UpdateMainservice.as_view() , name='updatesub_serlizer'),

]
