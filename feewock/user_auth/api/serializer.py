from rest_framework.serializers import ModelSerializer
import random
from datetime import datetime , timedelta
from django.conf import settings
from user_auth.models import UserModel
from rest_framework import serializers
from user_auth.utils import send_otp
from user_auth.models import UserModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only = True,
        min_length = settings.MIN_PASSWORD_LENGTH,
        error_messages = {
            "min_length":"password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        }
    )

    password2 = serializers.CharField(
        write_only = True,
        min_length = settings.MIN_PASSWORD_LENGTH,
        error_messages = {
            "min_length":"password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        }
    )

    class Meta:
        model = UserModel
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "location",
            "phone_number",
            "is_active",
            "password1",
            "password2"
        )
        read_only_fields = ["id"]

    def validate(self , data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("passsword do not match")
        return data
    
    def create(self , validated_data):
        otp = random.randint(1000,9999)
        otp_expiry = datetime.now() + timedelta(minutes=10)
        user = UserModel(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            location = validated_data["location"],
            phone_number = validated_data["phone_number"],
            email = validated_data["email"],
            otp = otp,
            otp_expiry = otp_expiry,
            max_otp_try = settings.MAX_OTP_TRY
        )
        user.set_password(validated_data["password1"])
        user.save()
        send_otp(validated_data["phone_number"],otp)
        return user


class CustomerTokenObtainPairSerialzer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.is_superuser:
            data['is_admin'] = True
        elif hasattr(user , 'employee'):
            data['is_employee'] = True
        else:
            data['is_regular_user'] = True
            data['id'] = user.id
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['email'] = user.email  
            data['number'] = user.phone_number
            data['location'] = user.location
            data['is_active'] = user.is_active
        return data

    