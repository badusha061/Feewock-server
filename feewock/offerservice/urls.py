from django.urls import path
from .views import CreateOfferService , UpdateOfferService , ListOfferService

urlpatterns = [ 

   path('list',  ListOfferService.as_view(), name='create_offserservice'),
   path('create',  CreateOfferService.as_view(), name='create_offserservice'),
    path('updateoffer/<int:pk>/', UpdateOfferService.as_view(), name='updateofferservice_serlizer'),
]
