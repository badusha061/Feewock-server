from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager , Permission
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator , validate_email
from django.contrib.auth import get_user_model
from .common_auth import UserManager



phone_regex = RegexValidator(
    regex=r"^\d{10}", message="Phone number must be 10 digits only."
)


ROLE_CHOICES = [
   (1, 'ADMIN'),
   (2, 'EMPLOYEE'),
   (3, 'USER'),
]


class UserModel(AbstractBaseUser , PermissionsMixin):
    role = models.IntegerField(choices = ROLE_CHOICES , null = True)
    first_name = models.CharField(max_length=50,blank = True,null = True)
    last_name = models.CharField( max_length=50,blank = True,null = True)
    email = models.EmailField(
        max_length=50,
        blank = True,
        null = True,
        validators = [validate_email], 
        unique = True,
        
        )
    location = models.CharField(max_length=150,null = True)
    phone_number = models.CharField(
        max_length=50,
        blank = True,
        null = True,
        unique = True,
        validators = [phone_regex]
        )
    images = models.ImageField(upload_to='Images',null= True , blank=True)
    otp = models.CharField( max_length=6 , null = True)
    otp_expiry = models.DateTimeField(blank = True,null = True)
    max_otp_try = models.CharField(default = settings.MAX_OTP_TRY , max_length=2)
    otp_time_out = models.DateTimeField(blank = True,null = True)

    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    user_registered_at = models.DateTimeField(auto_now_add = True)

    group = models.ManyToManyField(
        Permission,
        related_name='user_model_permission',
    )

    USERNAME_FIELD =  "email"

    objects = UserManager()


    def __str__(self) -> str:
        return self.email
    
