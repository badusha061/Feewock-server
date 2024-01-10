from django.shortcuts import render
from .serializer import MainServiceSerializer , SubServiceSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import MainService

# Create your views here.

class CreateMainService(ListCreateAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


class UpdateMainservice(RetrieveUpdateDestroyAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


class CreateSubService(ListCreateAPIView):
    queryset = MainService.objects.all()
    serializer_class = SubServiceSerializer


class UpdateSubservice(RetrieveUpdateDestroyAPIView):
    queryset = MainService.objects.all()
    serializer_class = SubServiceSerializer
