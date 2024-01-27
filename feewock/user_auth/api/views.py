from rest_framework import generics , status , viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import random 
import datetime 
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import action
from .serializer import UserSerializer
from user_auth.models import UserModel
from user_auth.utils import send_otp
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import CustomerTokenObtainPairSerialzer , UserIndvualSerializers , UserIndvualImageSerializers
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset   = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(detail=True , methods=["PATCH"])
    def verify_otp(self , request , pk = None):
        instance = self.get_object()
        if(
            not instance.is_active
            and  instance.otp == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_active = True
            instance.otp_expiry = None
            instance.max_otp_try = settings.MAX_OTP_TRY
            instance.otp_max_out = None
            instance.save()
            return Response(
                "Successfully verifie the user",status= status.HTTP_200_OK
            )
        return Response(
            "User Active or Please enter the correct otp",
            status=  status.HTTP_400_BAD_REQUEST
        )
    @action(detail=True , methods= ["PATCH"])
    def generate_otp(self,request , pk = None):
        instance = self.get_object()
        if int(instance.max_otp_try) == 0:
            return Response(
                "max otp try reached , try after an hour",
                status= status.HTTP_400_BAD_REQUEST
            )
        otp = random.randint(1000,9999)
        otp_exipry = timezone.now() + datetime.timedelta(minutes=10)
        max_otp_try = int(instance.max_otp_try) - 1
        instance.otp = otp
        instance.otp_expiry = otp_exipry
        instance.max_otp_try = max_otp_try
        if max_otp_try == 0:
            otp_max_out = timezone.now() + datetime.timedelta(hours=1)
            instance.otp_max_out = otp_max_out
        elif max_otp_try == -1:
            instance.max_otp_try = settings.MAX_OTP_TRY
        else:
            instance.otp_max_out = None
            instance.max_otp_try = max_otp_try
        instance.save()
        send_otp(instance.phone_number , otp)
        return Response("Successfully generate new otp ", status= status.HTTP_200_OK)
    


class CustomerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerialzer



@permission_classes([IsAuthenticated])
class UserIndivualView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserIndvualSerializers
    queryset = UserModel.objects.all()


@permission_classes([IsAuthenticated])
class UserIndivualImage(RetrieveUpdateDestroyAPIView):
    serializer_class = UserIndvualImageSerializers
    queryset = UserModel.objects.all()