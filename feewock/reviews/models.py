from django.db import models
from user_auth.models import UserModel
from employee_auth.models import Employees
# Create your models here.


class Reviews(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name = 'user_reviews')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE,related_name='employee_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=False)
    def __str__(self) -> str:
        return self.content


