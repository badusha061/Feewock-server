from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,Permission 
from django.contrib.auth.models import Group
from user_auth.models import UserManager
from django.core.validators import RegexValidator , validate_email
from django.conf import settings
from user_auth.models import UserModel

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
    username = models.CharField(max_length = 50,null= True)
    email = models.EmailField(max_length=254, unique =  True , validators =[validate_email],null=True)
    gender = models.CharField(max_length=1 , choices = GENDER_CHOICES,null = True)
    phone_number = models.BigIntegerField(unique =  True , validators =[phone_regex] ,null = True)
    dob = models.DateField(verbose_name = "Date of birth",null = True)
    address = models.TextField(max_length=250,null = True)
    city = models.CharField(max_length = 50,null = True)
    state = models.CharField(max_length = 50,null = True)
    type_of_work = models.CharField(
        max_length = 2,
        choices = TYPE_OF_WORK_CHOICES,
        default = 'FT'
        ,null = True

    )
    adhar_number = models.BigIntegerField(unique=True,null = True)
    images = models.ImageField(upload_to='Image',blank=True)
    bank_details = models.ForeignKey(BankDetails,on_delete=models.CASCADE, null = True)
    is_active = models.BooleanField(default= False)
    position = models.ManyToManyField(EmployeePostion,blank=True)
    location = models.CharField(max_length=50,null=True)
    otp = models.CharField(max_length = 4,null=True)
    otp_expiry = models.DateTimeField(blank = True,null = True)
    max_otp_try = models.CharField(default = settings.MAX_OTP_TRY , max_length=2,null=True)
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
    

