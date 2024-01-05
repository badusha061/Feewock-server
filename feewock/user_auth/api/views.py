from rest_framework import generics , status
from rest_framework.response import Response
from .serializer import UserSerialzer
from rest_framework.views import APIView

class Registrations(APIView):
    def post(self,request):
        print(request.data)
        serializer_class = UserSerialzer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data , status=status.HTTP_201_CREATED)
        else:
            print(serializer_class.errors,'the error message is the ')
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
