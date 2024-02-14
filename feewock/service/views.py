from django.shortcuts import render
from .serializer import MainServiceSerializer , SubServiceSerializer , EmployeePostionsSubService , SubServiceSerializerFetch , FetchMainService
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , ListAPIView
from .models import MainService , SubService 
from employee_auth.models import EmployeePostion
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser , IsAuthenticated , AllowAny
from rest_framework.decorators import permission_classes

# Create your views here.

@permission_classes([IsAdminUser])
class CreateMainService(ListCreateAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


@permission_classes([IsAdminUser])
class UpdateMainservice(RetrieveUpdateDestroyAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer


@permission_classes([IsAdminUser])
class ListSubService(ListCreateAPIView):  
    queryset =SubService.objects.all()
    serializer_class = SubServiceSerializerFetch


class ListSubServiceEmployee(ListCreateAPIView):  
    queryset =SubService.objects.all()
    serializer_class = SubServiceSerializerFetch

@permission_classes([IsAdminUser])
class CreateSubService(ListCreateAPIView):
    parser_classes = [MultiPartParser , FormParser]
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer


@permission_classes([IsAdminUser])
class UpdateSubservice(RetrieveUpdateDestroyAPIView):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer


class Postions(ListCreateAPIView):
    queryset =EmployeePostion.objects.all()
    serializer_class = EmployeePostionsSubService


class UpdatePositions(RetrieveUpdateDestroyAPIView):
    queryset = EmployeePostion.objects.all()
    serializer_class = EmployeePostionsSubService

@permission_classes([IsAuthenticated])
class ListingMainService(ListAPIView):
    queryset = MainService.objects.all()
    serializer_class = FetchMainService
    

class ListingUserMainService(ListAPIView):
    queryset = MainService.objects.all()
    serializer_class = FetchMainService
    