from django.db import models

# Create your models here.

class UserBanner(models.Model):
    titile = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='Banner_image')

    def __str__(self) -> str:
        return self.titile

class EmployeeBanner(models.Model):
    titile = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='Banner_image')
    
    def __str__(self) -> str:
        return self.titile