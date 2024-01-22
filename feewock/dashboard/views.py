from django.shortcuts import render
from rest_framework import generics , status
from rest_framework import viewsets
from rest_framework.response import Response
from user_auth.models import UserModel
from user_auth.api.serializer import UserSerializer
from employee_auth.serializer import EmployeeSerializer
from employee_auth.models import Employees
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
# Create your views here.

@permission_classes([IsAdminUser])
class UserListView(generics.ListAPIView):
    def get_queryset(self):
        return UserModel.objects.filter(role = 3)
    serializer_class = UserSerializer
    

class UserBlockUnblock(viewsets.ViewSet):
    def block(self , request , pk= None):
        try:
            user_obj = UserModel.objects.get(id = pk)
            user_obj.is_active = False
            user_obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def unblock(self,request,pk=None):
        try:
            user_obj = UserModel.objects.get(id = pk)
            user_obj.is_active= True
            user_obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status= status.HTTP_400_BAD_REQUEST)
     
class EmployeesListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return Employees.objects.filter(role = 2)
    
class EmployeesIndvualView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return Employees.objects.filter(role = 2)    

class EmployeeBlockUnblock(viewsets.ViewSet):
    def block(self , request , pk= None):
        try:
            user_obj = Employees.objects.get(id = pk)
            user_obj.is_active = False
            user_obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def unblock(self,request,pk=None):
        try:
            user_obj = Employees.objects.get(id = pk)
            user_obj.is_active= True
            user_obj.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status= status.HTTP_400_BAD_REQUEST)