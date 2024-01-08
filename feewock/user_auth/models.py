from django.contrib.auth.models import AbstractUser , Group , Permission
from django.db import models
from django.conf import settings

class Customer(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    number = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    otp = models.CharField(max_length = 6 , null = True , blank = True)
    otp_expiry = models.DateTimeField(null=True,blank = True)
    max_otp_try = models.CharField( max_length=2 , default = settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank = True , null = True)
    groups = models.ManyToManyField(
        Group,
        related_name="customer_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customer_user_permissions",
        blank=True,
    )


    def __str__(self) -> str:
        return self.first_name  
