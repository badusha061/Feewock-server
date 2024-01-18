from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , ListAPIView
from .models import OfferService
from .serializer import OfferServiceSerializer , OfferServiceSerializerList

# Create your views here.

class ListOfferService(ListCreateAPIView):
    queryset = OfferService.objects.all()
    serializer_class = OfferServiceSerializerList

class CreateOfferService(ListCreateAPIView):
    queryset = OfferService.objects.all()
    serializer_class = OfferServiceSerializer


class UpdateOfferService(RetrieveUpdateDestroyAPIView):
    queryset = OfferService.objects.all()
    serializer_class = OfferServiceSerializer
