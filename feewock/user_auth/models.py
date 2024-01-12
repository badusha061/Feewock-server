from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager , Permission
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator , validate_email

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="Phone number must be 10 digits only."
)


class UserManager(BaseUserManager):
    def create_user(self , email , password = None):
        if not email:
            raise ValueError("User must have a email")
        user = self.model(email = email)
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self, email , password):
        user = self.create_user(
            email=email , password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user

class UserModel(AbstractBaseUser , PermissionsMixin):
    first_name = models.CharField(max_length=50,blank = True,null = True)
    last_name = models.CharField( max_length=50,blank = True,null = True)
    email = models.EmailField(
        max_length=50,
        blank = True,
        null = True,
        validators = [validate_email], 
        unique = True,
        
        )
    location = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=50,
        blank = True,
        null = True,
        unique = True,
        validators = [phone_regex]
        )
    otp = models.CharField( max_length=6)
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