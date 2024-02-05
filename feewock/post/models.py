from django.db import models
from employee_auth.models import Employees
from user_auth.models import UserModel
from django.db.models import Count
# Create your models here.


class Posts(models.Model):
    employee = models.ForeignKey(Employees, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    captions = models.TextField()
    image = models.ImageField(upload_to='images',null=True)

    def __str__(self) -> str:
        return self.employee.username
    
    def likes_count(self):
        return self.likes.count()

    
class Likes(models.Model):
    user = models.ForeignKey(UserModel, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name = 'likes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name
    
    