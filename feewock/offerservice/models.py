from django.db import models
from service.models import SubService
# Create your models here.

class OfferService(models.Model):
    name = models.CharField(max_length=50, unique = True , blank = True , null = True)
    image = models.ImageField(upload_to='offerimage', blank=True , null=True)
    service = models.ForeignKey(SubService, on_delete=models.CASCADE,related_name='service' , null = True)
    description = models.TextField()
    is_active = models.BooleanField(default = True)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.IntegerField(null = True)

    def __str__(self) -> str:
        return self.name
