from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,Permission 
from django.contrib.auth.models import Group
from user_auth.models import UserManager
from django.core.validators import RegexValidator , validate_email
from django.conf import settings

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="Phone number must be 10 digits only."
)

# Create your models here.

GENDER_CHOICES = [
   ('M', 'Male'),
   ('F', 'Female'),
   ('N', 'Non-binary'),
   ('P', 'Prefer not to say'),
]

TYPE_OF_WORK_CHOICES = [
  ('FT', 'Full Time'),
  ('PT', 'Part Time'),
  ('CT', 'Contract'),
  ('IT', 'Internship'),
]


class BankDetails(models.Model):
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length= 20)
    

class EmployeePostion(models.Model):
    name = models.CharField(max_length = 50,null = True, blank = True,unique = True)
    is_active = models.BooleanField(default = True)

    # def __str__(self) -> str:
    #     return self.postion_name



class Employees(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254, unique =  True , validators =[validate_email])
    gender = models.CharField(max_length=1 , choices = GENDER_CHOICES)
    phone_number = models.BigIntegerField(unique =  True , validators =[phone_regex] )
    dob = models.DateField(verbose_name = "Date of birth")
    address = models.TextField(max_length=250)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    type_of_work = models.CharField(
        max_length = 2,
        choices = TYPE_OF_WORK_CHOICES,
        default = 'FT'
    )
    adhar_number = models.BigIntegerField(unique=True)
    images = models.ImageField(upload_to='Image',blank=True)
    bank_details = models.ForeignKey(BankDetails,on_delete=models.CASCADE, null = True)
    is_active = models.BooleanField(default= False)
    position = models.ManyToManyField(EmployeePostion)
    location = models.CharField(max_length=50,null=True)
    otp = models.CharField(max_length = 4,null=True)
    otp_expiry = models.DateTimeField(blank = True,null = True)
    max_otp_try = models.CharField(default = settings.MAX_OTP_TRY , max_length=2)
    otp_time_out = models.DateTimeField(blank = True,null = True)
    groups = models.ManyToManyField(
        Permission,
        related_name='employees_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='employees_permissions',
    )

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email
    

