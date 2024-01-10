from django.shortcuts import render
from rest_framework import generics , status
from rest_framework import viewsets
from rest_framework.response import Response
from user_auth.models import UserModel
from user_auth.api.serializer import UserSerializer
# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
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
     