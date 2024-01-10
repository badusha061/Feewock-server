from django.db import models

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
    postion_name = models.CharField(max_length = 50,null = True, blank = True)
    postion_titile = models.TextField(max_length=255 , null = True , blank = True)

class Employees(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254, unique =  True)
    gender = models.CharField(max_length=1 , choices = GENDER_CHOICES)
    phone_number = models.BigIntegerField(unique =  True)
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
    images = models.ImageField(upload_to='Image')
    bank_details = models.ForeignKey(BankDetails,on_delete=models.CASCADE, null = True)
    is_active = models.BooleanField(default= False)
    position = models.ForeignKey(EmployeePostion, on_delete=models.CASCADE , null = True)
    password = models.CharField(max_length = 50)
    
    

