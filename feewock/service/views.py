from django.shortcuts import render
from .serializer import MainServiceSerializer , SubServiceSerializer , EmployeePostionsSubService 
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import MainService , SubService 
from employee_auth.models import EmployeePostion
# Create your views here.

class CreateMainService(ListCreateAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


class UpdateMainservice(RetrieveUpdateDestroyAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


class CreateSubService(ListCreateAPIView):
    queryset =SubService.objects.all()
    serializer_class = SubServiceSerializer
    

class UpdateSubservice(RetrieveUpdateDestroyAPIView):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer


class Postions(ListCreateAPIView):
    queryset =EmployeePostion.objects.all()
    serializer_class = EmployeePostionsSubService


class UpdatePositions(RetrieveUpdateDestroyAPIView):
    queryset = EmployeePostion.objects.all()
    serializer_class = EmployeePostionsSubService