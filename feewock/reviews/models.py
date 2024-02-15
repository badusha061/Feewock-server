from django.db import models
from user_auth.models import UserModel
from employee_auth.models import Employees
# Create your models here.


class EmployeeReviews(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name = 'user_reviews')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE,related_name='employee_reviews')
    content = models.TextField()
    star_rating = models.IntegerField(default= 0 , choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.content


