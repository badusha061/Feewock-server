from django.db import models
from employee_auth.models import Employees

# Create your models here.


class Posts(models.Model):
    employee = models.ForeignKey(Employees, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    captions = models.TextField()

    def __str__(self) -> str:
        return self.employee.username
    
class Likes(models.Model):
    employee = models.ForeignKey(Employees, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name = 'likes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.employee.username