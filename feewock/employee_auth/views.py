from django.shortcuts import render
from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView 
from rest_framework import generics , status , viewsets
from .serializer import EmployeeSerializer
from .models import Employees
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response 
import random
import datetime 
from django.utils import timezone
from  django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


class Employees(viewsets.ModelViewSet):
    try:
        queryset = Employees.objects.all()
        serializer_class = EmployeeSerializer
    except Exception as e:
        print(e)

    @action(detail=True , methods=["PATCH"])
    def generate_otp(self , request , pk):
        instance = self.get_object()
        if (int(instance.max_otp_try)) == 0:
            return Response (
                "max otp try reached , try after an hour"
            )
        otp = random.randint(1000,9999)
        otp_exipry = timezone.now() + datetime.timedelta(minutes=2)
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
        subject = 'YOUR ACCOUNT VERIFICATION EMAIL'
        message = f'{otp}'
        email_from = settings.EMAIL_HOST_USER
        context ={
            "username":instance.username,
            "otp_message":message
        }
        html_messages = render_to_string("email.html",context=context)
        plain_message = strip_tags(html_messages)
        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=email_from,
            to=[instance.email]
        )
        message.attach_alternative(html_messages,"text/html")
        message.send()
        return Response("Successfully generate new otp ", status= status.HTTP_200_OK)
    
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
                "Successfully verifie the Employee",status= status.HTTP_200_OK
            )
        return Response(
            "Employee Active or Please enter the correct otp",
            status=  status.HTTP_400_BAD_REQUEST
        )