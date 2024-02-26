from django.db import models

# Create your models here.


class MainService(models.Model):
    name = models.CharField(max_length = 50,null = True , blank = True , unique = True)
    is_active = models.BooleanField(default = True)

    def delete(self , using = None , keep_parents = False):
        self.is_active = False
        self.save()
    # def __str__(self) -> str:
    #     return self.name
    
    
class SubService(models.Model):
    name = models.CharField(max_length = 50 , blank = True , null = True , unique = True)
    Image = models.ImageField(upload_to='Image',blank=True,null=True)
    mainservice = models.ForeignKey(MainService, on_delete=models.CASCADE,null = True,related_name='subservice')
    is_active = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.name

















